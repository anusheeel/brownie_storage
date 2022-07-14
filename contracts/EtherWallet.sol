// SPDX-License-Identifier: Anusheel
pragma solidity >=0.6.0 <0.9.0;

contract EtherWallet {
    address payable public grid_owner;

    constructor() {
        grid_owner = payable(msg.sender);
    }

    receive() external payable {}

    function withdraw(uint256 _amount) external {
        require(
            msg.sender == grid_owner,
            "Only the owner can call this method."
        );
        payable(msg.sender).transfer(_amount);
    }

    // view represents read-only mode
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
