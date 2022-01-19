# High Gas Agent

## Description

This agent detects transactions with high gas consumption

## Supported Chains

- Ethereum

## Supported Network
- Mainnet
- Rinkeby

## Alerts

- Alert when authorized address send transaction to multisig address
- SeverityType is always set to Info

# Installation
- npx forta-agent@latest init --python

- npm install

# Set config

forta.config.json is located to ~/.forta folder,
- import infura-rpc to jsonRpcUrl

# run the test
npm test

# start script
npm start
