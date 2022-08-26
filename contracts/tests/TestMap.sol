//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.16;

import "@openzeppelin/contracts/utils/Counters.sol";

import {MemberMap} from "../libraries/MemberMap.sol";

contract TestMap {
    using MemberMap for MemberMap.Map;
    using MemberMap for MemberMap.Membership;
    using Counters for Counters.Counter;

    MemberMap.Map private map;
    Counters.Counter private counter;

    constructor() {
        map.add(address(0), "", counter.current());
        counter.increment();
    }

    function get(uint256 id) public view returns (MemberMap.Membership memory) {
        return map.getMembership(id);
    }

    function getUsername(uint256 id) public view returns (string memory) {
        return map.getMembership(id).username;
    }

    function size() public view returns (uint256) {
        return map.size();
    }

    function exist(uint256 id) public view returns (bool) {
        return map.exist(id);
    }

    function add(
        address member,
        string memory username,
        uint256 id
    ) public {
        map.add(member, username, id);
    }

    function update(uint256 id, string memory username) public {
        map.updateMembership(id, username);
    }

    function remove(uint256 id) public {
        map.remove(id);
    }
}
