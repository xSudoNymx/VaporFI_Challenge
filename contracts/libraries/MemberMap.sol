//SPDX-License-Identifier: Unlicense

pragma solidity ^0.8.16;

library MemberMap {
    struct Map {
        Membership[] memberships;
        mapping(address => uint256) memberId;
        mapping(uint256 => uint256) indexOf;
    }

    struct Membership {
        address member;
        string username;
        uint256 creationDate;
        uint256 expirationDate;
    }

    function exist(Map storage map, uint256 id) public view returns (bool) {
        return map.indexOf[id] != 0;
    }

    function duplicateMember(Map storage map, address member)
        private
        view
        returns (bool)
    {
        return map.memberId[member] != 0;
    }

    function size(Map storage map) public view returns (uint256) {
        return map.memberships.length - 1;
    }

    function getMembership(Map storage map, uint256 id)
        public
        view
        returns (Membership storage)
    {
        require(exist(map, id), "Membership Doesn't Exist");
        uint256 index = map.indexOf[id];
        return (map.memberships[index]);
    }

    function add(
        Map storage map,
        address member,
        string memory username,
        uint256 id
    ) public {
        require(!exist(map, id), "ID Exists");
        require(!duplicateMember(map, member), "Member Exists");
        Membership memory membership = Membership({
            member: member,
            username: username,
            creationDate: block.timestamp,
            expirationDate: block.timestamp + 30 days
        });

        map.indexOf[id] = map.memberships.length;
        map.memberId[membership.member] = id;
        map.memberships.push(membership);
    }

    // update a membership username
    function updateMembership(
        Map storage map,
        uint256 id,
        string memory username
    ) public {
        require(exist(map, id), "Membership Doesn't Exist");
        uint256 index = map.indexOf[id];
        require(
            map.memberships[index].member == msg.sender,
            "You are not the owner of this membership"
        );
        map.memberships[index].username = username;
    }

    function remove(Map storage map, uint256 id) public {
        require(exist(map, id), "Membership Doesn't Exist");

        uint256 index = map.indexOf[id];
        uint256 lastIndex = map.memberships.length - 1;
        uint256 lastIndexId = map.memberId[map.memberships[lastIndex].member];

        // Remove from indexOf
        map.indexOf[lastIndexId] = index;
        delete map.indexOf[id];
        map.memberships[index] = map.memberships[lastIndex];
        map.memberships.pop();
    }
}
