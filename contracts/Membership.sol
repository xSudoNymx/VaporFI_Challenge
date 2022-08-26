//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.16;
import "@upgrade/contracts/proxy/utils/Initializable.sol";
import "@upgrade/contracts/access/OwnableUpgradeable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

import {MemberMap} from "./libraries/MemberMap.sol";

contract Membership is Initializable, OwnableUpgradeable {
    using MemberMap for MemberMap.Map;
    using MemberMap for MemberMap.Membership;
    using Counters for Counters.Counter;

    Counters.Counter private counter;
    MemberMap.Map private map;

    function initialize() public initializer {
        __Ownable_init();
        map.add(address(0), "", counter.current());
        counter.increment();
    }

    // create a new membership
    function createMembership(address member, string memory username)
        public
        onlyOwner
    {
        map.add(member, username, counter.current());
        counter.increment();
    }

    //create multiple new memberships
    function createMemberships(
        address[] memory members,
        string[] memory usernames
    ) public onlyOwner {
        require(
            members.length == usernames.length,
            "Members and Usernames must be the same length"
        );
        for (uint256 i = 0; i < members.length; i++) {
            createMembership(members[i], usernames[i]);
        }
    }

    // get a membership by id
    function getMembership(uint256 id)
        public
        view
        returns (MemberMap.Membership memory)
    {
        return map.getMembership(id);
    }

    // update a membership username
    function updateMembership(uint256 id, string memory username) public {
        map.updateMembership(id, username);
    }

    // remove the membership of the given id
    function deleteMembership(uint256 id) public onlyOwner {
        map.remove(id);
    }
}
