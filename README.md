# VaporFi Solidity Challenge
## Note: Project uses brownie to build, deploy, test, and upgrade

### How to run 

1. add private keys to .env File

Build Contracts:

    $ brownie compile --all
    
Run Deploy + Upgrade:

    $ brownie run '.\scripts\01_deply_and_upgrade_ membership.py'
    
Run Tests:

    $ brownie test 
    
Run Gas Check:

    $ brownie test --gas  
   
