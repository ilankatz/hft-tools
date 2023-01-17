weth_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "tokenName", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "spender", "type": "address"},
            {"name": "value", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"name": "success", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "totalTokensIssued", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "from", "type": "address"},
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"name": "success", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "decimalPlaces", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "tokenSymbol", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "payable": True,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [
            {"name": "owner", "type": "address"},
            {"name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"name": "remaining", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

price_feed_abi = [
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "description",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint80", "name": "_roundId", "type": "uint80"}],
        "name": "getRoundData",
        "outputs": [
            {"internalType": "uint80", "name": "roundId", "type": "uint80"},
            {"internalType": "int256", "name": "answer", "type": "int256"},
            {"internalType": "uint256", "name": "startedAt", "type": "uint256"},
            {"internalType": "uint256", "name": "updatedAt", "type": "uint256"},
            {"internalType": "uint80", "name": "answeredInRound", "type": "uint80"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "latestRoundData",
        "outputs": [
            {"internalType": "uint80", "name": "roundId", "type": "uint80"},
            {"internalType": "int256", "name": "answer", "type": "int256"},
            {"internalType": "uint256", "name": "startedAt", "type": "uint256"},
            {"internalType": "uint256", "name": "updatedAt", "type": "uint256"},
            {"internalType": "uint80", "name": "answeredInRound", "type": "uint80"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "version",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]

erc20_abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [
            {"internalType": "uint256", "name": "remaining", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "success", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "balance", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {"internalType": "uint8", "name": "decimalPlaces", "type": "uint8"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
        ],
        "name": "decreaseApproval",
        "outputs": [{"internalType": "bool", "name": "success", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
        ],
        "name": "increaseApproval",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "tokenName", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {"internalType": "string", "name": "tokenSymbol", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {"internalType": "uint256", "name": "totalTokensIssued", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "success", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
        ],
        "name": "transferAndCall",
        "outputs": [{"internalType": "bool", "name": "success", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "success", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

lending_pool_addresses_provider_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "hasProxy",
                "type": "bool",
            },
        ],
        "name": "AddressSet",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            }
        ],
        "name": "ConfigurationAdminUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            }
        ],
        "name": "EmergencyAdminUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            }
        ],
        "name": "LendingPoolCollateralManagerUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            }
        ],
        "name": "LendingPoolConfiguratorUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            }
        ],
        "name": "LendingPoolUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            }
        ],
        "name": "LendingRateOracleUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "newMarketId",
                "type": "string",
            }
        ],
        "name": "MarketIdSet",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            }
        ],
        "name": "PriceOracleUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "id",
                "type": "bytes32",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newAddress",
                "type": "address",
            },
        ],
        "name": "ProxyCreated",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "id", "type": "bytes32"}],
        "name": "getAddress",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getEmergencyAdmin",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLendingPool",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLendingPoolCollateralManager",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLendingPoolConfigurator",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLendingRateOracle",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getMarketId",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getPoolAdmin",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getPriceOracle",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "id", "type": "bytes32"},
            {"internalType": "address", "name": "newAddress", "type": "address"},
        ],
        "name": "setAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "id", "type": "bytes32"},
            {"internalType": "address", "name": "impl", "type": "address"},
        ],
        "name": "setAddressAsProxy",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "admin", "type": "address"}],
        "name": "setEmergencyAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "manager", "type": "address"}],
        "name": "setLendingPoolCollateralManager",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "configurator", "type": "address"}
        ],
        "name": "setLendingPoolConfiguratorImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "pool", "type": "address"}],
        "name": "setLendingPoolImpl",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "lendingRateOracle", "type": "address"}
        ],
        "name": "setLendingRateOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "string", "name": "marketId", "type": "string"}],
        "name": "setMarketId",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "admin", "type": "address"}],
        "name": "setPoolAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "priceOracle", "type": "address"}
        ],
        "name": "setPriceOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

lending_pool_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "borrowRateMode",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "borrowRate",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "uint16",
                "name": "referral",
                "type": "uint16",
            },
        ],
        "name": "Borrow",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "onBehalfOf",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "uint16",
                "name": "referral",
                "type": "uint16",
            },
        ],
        "name": "Deposit",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "target",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "initiator",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "asset",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "premium",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint16",
                "name": "referralCode",
                "type": "uint16",
            },
        ],
        "name": "FlashLoan",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "collateralAsset",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "debtAsset",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "debtToCover",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "liquidatedCollateralAmount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "liquidator",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "receiveAToken",
                "type": "bool",
            },
        ],
        "name": "LiquidationCall",
        "type": "event",
    },
    {"anonymous": False, "inputs": [], "name": "Paused", "type": "event"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
        ],
        "name": "RebalanceStableBorrowRate",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "repayer",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "Repay",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "liquidityRate",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "stableBorrowRate",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "variableBorrowRate",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "liquidityIndex",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "variableBorrowIndex",
                "type": "uint256",
            },
        ],
        "name": "ReserveDataUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
        ],
        "name": "ReserveUsedAsCollateralDisabled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
        ],
        "name": "ReserveUsedAsCollateralEnabled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "rateMode",
                "type": "uint256",
            },
        ],
        "name": "Swap",
        "type": "event",
    },
    {"anonymous": False, "inputs": [], "name": "Unpaused", "type": "event"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "reserve",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
            },
        ],
        "name": "Withdraw",
        "type": "event",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "uint256", "name": "interestRateMode", "type": "uint256"},
            {"internalType": "uint16", "name": "referralCode", "type": "uint16"},
            {"internalType": "address", "name": "onBehalfOf", "type": "address"},
        ],
        "name": "borrow",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "address", "name": "onBehalfOf", "type": "address"},
            {"internalType": "uint16", "name": "referralCode", "type": "uint16"},
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "nonpayable", #***************Should be marked 'payable'?***************
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "uint256", "name": "balanceFromAfter", "type": "uint256"},
            {"internalType": "uint256", "name": "balanceToBefore", "type": "uint256"},
        ],
        "name": "finalizeTransfer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "receiverAddress", "type": "address"},
            {"internalType": "address[]", "name": "assets", "type": "address[]"},
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "modes", "type": "uint256[]"},
            {"internalType": "address", "name": "onBehalfOf", "type": "address"},
            {"internalType": "bytes", "name": "params", "type": "bytes"},
            {"internalType": "uint16", "name": "referralCode", "type": "uint16"},
        ],
        "name": "flashLoan",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getAddressesProvider",
        "outputs": [
            {
                "internalType": "contract ILendingPoolAddressesProvider",
                "name": "",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
        "name": "getConfiguration",
        "outputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "data", "type": "uint256"}
                ],
                "internalType": "struct DataTypes.ReserveConfigurationMap",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
        "name": "getReserveData",
        "outputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "data",
                                "type": "uint256",
                            }
                        ],
                        "internalType": "struct DataTypes.ReserveConfigurationMap",
                        "name": "configuration",
                        "type": "tuple",
                    },
                    {
                        "internalType": "uint128",
                        "name": "liquidityIndex",
                        "type": "uint128",
                    },
                    {
                        "internalType": "uint128",
                        "name": "variableBorrowIndex",
                        "type": "uint128",
                    },
                    {
                        "internalType": "uint128",
                        "name": "currentLiquidityRate",
                        "type": "uint128",
                    },
                    {
                        "internalType": "uint128",
                        "name": "currentVariableBorrowRate",
                        "type": "uint128",
                    },
                    {
                        "internalType": "uint128",
                        "name": "currentStableBorrowRate",
                        "type": "uint128",
                    },
                    {
                        "internalType": "uint40",
                        "name": "lastUpdateTimestamp",
                        "type": "uint40",
                    },
                    {
                        "internalType": "address",
                        "name": "aTokenAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "stableDebtTokenAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "variableDebtTokenAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "interestRateStrategyAddress",
                        "type": "address",
                    },
                    {"internalType": "uint8", "name": "id", "type": "uint8"},
                ],
                "internalType": "struct DataTypes.ReserveData",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
        "name": "getReserveNormalizedIncome",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
        "name": "getReserveNormalizedVariableDebt",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getReservesList",
        "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getUserAccountData",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "totalCollateralETH",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "totalDebtETH", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "availableBorrowsETH",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "currentLiquidationThreshold",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "ltv", "type": "uint256"},
            {"internalType": "uint256", "name": "healthFactor", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getUserConfiguration",
        "outputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "data", "type": "uint256"}
                ],
                "internalType": "struct DataTypes.UserConfigurationMap",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "reserve", "type": "address"},
            {"internalType": "address", "name": "aTokenAddress", "type": "address"},
            {"internalType": "address", "name": "stableDebtAddress", "type": "address"},
            {
                "internalType": "address",
                "name": "variableDebtAddress",
                "type": "address",
            },
            {
                "internalType": "address",
                "name": "interestRateStrategyAddress",
                "type": "address",
            },
        ],
        "name": "initReserve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "collateralAsset", "type": "address"},
            {"internalType": "address", "name": "debtAsset", "type": "address"},
            {"internalType": "address", "name": "user", "type": "address"},
            {"internalType": "uint256", "name": "debtToCover", "type": "uint256"},
            {"internalType": "bool", "name": "receiveAToken", "type": "bool"},
        ],
        "name": "liquidationCall",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "paused",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "address", "name": "user", "type": "address"},
        ],
        "name": "rebalanceStableBorrowRate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "uint256", "name": "rateMode", "type": "uint256"},
            {"internalType": "address", "name": "onBehalfOf", "type": "address"},
        ],
        "name": "repay",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "reserve", "type": "address"},
            {"internalType": "uint256", "name": "configuration", "type": "uint256"},
        ],
        "name": "setConfiguration",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bool", "name": "val", "type": "bool"}],
        "name": "setPause",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "reserve", "type": "address"},
            {
                "internalType": "address",
                "name": "rateStrategyAddress",
                "type": "address",
            },
        ],
        "name": "setReserveInterestRateStrategyAddress",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "bool", "name": "useAsCollateral", "type": "bool"},
        ],
        "name": "setUserUseReserveAsCollateral",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "uint256", "name": "rateMode", "type": "uint256"},
        ],
        "name": "swapBorrowRateMode",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
            {"internalType": "address", "name": "to", "type": "address"},
        ],
        "name": "withdraw",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

protocolDataProvider_abi = [{"inputs":[{"internalType":"contract ILendingPoolAddressesProvider","name":"addressesProvider","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ADDRESSES_PROVIDER","outputs":[{"internalType":"contract ILendingPoolAddressesProvider","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllATokens","outputs":[{"components":[{"internalType":"string","name":"symbol","type":"string"},{"internalType":"address","name":"tokenAddress","type":"address"}],"internalType":"struct AaveProtocolDataProvider.TokenData[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllReservesTokens","outputs":[{"components":[{"internalType":"string","name":"symbol","type":"string"},{"internalType":"address","name":"tokenAddress","type":"address"}],"internalType":"struct AaveProtocolDataProvider.TokenData[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"}],"name":"getReserveConfigurationData","outputs":[{"internalType":"uint256","name":"decimals","type":"uint256"},{"internalType":"uint256","name":"ltv","type":"uint256"},{"internalType":"uint256","name":"liquidationThreshold","type":"uint256"},{"internalType":"uint256","name":"liquidationBonus","type":"uint256"},{"internalType":"uint256","name":"reserveFactor","type":"uint256"},{"internalType":"bool","name":"usageAsCollateralEnabled","type":"bool"},{"internalType":"bool","name":"borrowingEnabled","type":"bool"},{"internalType":"bool","name":"stableBorrowRateEnabled","type":"bool"},{"internalType":"bool","name":"isActive","type":"bool"},{"internalType":"bool","name":"isFrozen","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"}],"name":"getReserveData","outputs":[{"internalType":"uint256","name":"availableLiquidity","type":"uint256"},{"internalType":"uint256","name":"totalStableDebt","type":"uint256"},{"internalType":"uint256","name":"totalVariableDebt","type":"uint256"},{"internalType":"uint256","name":"liquidityRate","type":"uint256"},{"internalType":"uint256","name":"variableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"stableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"averageStableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"liquidityIndex","type":"uint256"},{"internalType":"uint256","name":"variableBorrowIndex","type":"uint256"},{"internalType":"uint40","name":"lastUpdateTimestamp","type":"uint40"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"}],"name":"getReserveTokensAddresses","outputs":[{"internalType":"address","name":"aTokenAddress","type":"address"},{"internalType":"address","name":"stableDebtTokenAddress","type":"address"},{"internalType":"address","name":"variableDebtTokenAddress","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"address","name":"user","type":"address"}],"name":"getUserReserveData","outputs":[{"internalType":"uint256","name":"currentATokenBalance","type":"uint256"},{"internalType":"uint256","name":"currentStableDebt","type":"uint256"},{"internalType":"uint256","name":"currentVariableDebt","type":"uint256"},{"internalType":"uint256","name":"principalStableDebt","type":"uint256"},{"internalType":"uint256","name":"scaledVariableDebt","type":"uint256"},{"internalType":"uint256","name":"stableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"liquidityRate","type":"uint256"},{"internalType":"uint40","name":"stableRateLastUpdated","type":"uint40"},{"internalType":"bool","name":"usageAsCollateralEnabled","type":"bool"}],"stateMutability":"view","type":"function"}]
ui_abi = [{"inputs":[{"internalType":"contract IChainlinkAggregator","name":"_networkBaseTokenPriceInUsdProxyAggregator","type":"address"},{"internalType":"contract IChainlinkAggregator","name":"_marketReferenceCurrencyPriceInUsdProxyAggregator","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ETH_CURRENCY_UNIT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MKRAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_bytes32","type":"bytes32"}],"name":"bytes32ToString","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"contract ILendingPoolAddressesProvider","name":"provider","type":"address"}],"name":"getReservesData","outputs":[{"components":[{"internalType":"address","name":"underlyingAsset","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"uint256","name":"decimals","type":"uint256"},{"internalType":"uint256","name":"baseLTVasCollateral","type":"uint256"},{"internalType":"uint256","name":"reserveLiquidationThreshold","type":"uint256"},{"internalType":"uint256","name":"reserveLiquidationBonus","type":"uint256"},{"internalType":"uint256","name":"reserveFactor","type":"uint256"},{"internalType":"bool","name":"usageAsCollateralEnabled","type":"bool"},{"internalType":"bool","name":"borrowingEnabled","type":"bool"},{"internalType":"bool","name":"stableBorrowRateEnabled","type":"bool"},{"internalType":"bool","name":"isActive","type":"bool"},{"internalType":"bool","name":"isFrozen","type":"bool"},{"internalType":"uint128","name":"liquidityIndex","type":"uint128"},{"internalType":"uint128","name":"variableBorrowIndex","type":"uint128"},{"internalType":"uint128","name":"liquidityRate","type":"uint128"},{"internalType":"uint128","name":"variableBorrowRate","type":"uint128"},{"internalType":"uint128","name":"stableBorrowRate","type":"uint128"},{"internalType":"uint40","name":"lastUpdateTimestamp","type":"uint40"},{"internalType":"address","name":"aTokenAddress","type":"address"},{"internalType":"address","name":"stableDebtTokenAddress","type":"address"},{"internalType":"address","name":"variableDebtTokenAddress","type":"address"},{"internalType":"address","name":"interestRateStrategyAddress","type":"address"},{"internalType":"uint256","name":"availableLiquidity","type":"uint256"},{"internalType":"uint256","name":"totalPrincipalStableDebt","type":"uint256"},{"internalType":"uint256","name":"averageStableRate","type":"uint256"},{"internalType":"uint256","name":"stableDebtLastUpdateTimestamp","type":"uint256"},{"internalType":"uint256","name":"totalScaledVariableDebt","type":"uint256"},{"internalType":"uint256","name":"priceInMarketReferenceCurrency","type":"uint256"},{"internalType":"address","name":"priceOracle","type":"address"},{"internalType":"uint256","name":"variableRateSlope1","type":"uint256"},{"internalType":"uint256","name":"variableRateSlope2","type":"uint256"},{"internalType":"uint256","name":"stableRateSlope1","type":"uint256"},{"internalType":"uint256","name":"stableRateSlope2","type":"uint256"},{"internalType":"uint256","name":"baseStableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"baseVariableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"optimalUsageRatio","type":"uint256"},{"internalType":"bool","name":"isPaused","type":"bool"},{"internalType":"bool","name":"isSiloedBorrowing","type":"bool"},{"internalType":"uint128","name":"accruedToTreasury","type":"uint128"},{"internalType":"uint128","name":"unbacked","type":"uint128"},{"internalType":"uint128","name":"isolationModeTotalDebt","type":"uint128"},{"internalType":"uint256","name":"debtCeiling","type":"uint256"},{"internalType":"uint256","name":"debtCeilingDecimals","type":"uint256"},{"internalType":"uint8","name":"eModeCategoryId","type":"uint8"},{"internalType":"uint256","name":"borrowCap","type":"uint256"},{"internalType":"uint256","name":"supplyCap","type":"uint256"},{"internalType":"uint16","name":"eModeLtv","type":"uint16"},{"internalType":"uint16","name":"eModeLiquidationThreshold","type":"uint16"},{"internalType":"uint16","name":"eModeLiquidationBonus","type":"uint16"},{"internalType":"address","name":"eModePriceSource","type":"address"},{"internalType":"string","name":"eModeLabel","type":"string"},{"internalType":"bool","name":"borrowableInIsolation","type":"bool"}],"internalType":"struct IUiPoolDataProviderV3.AggregatedReserveData[]","name":"","type":"tuple[]"},{"components":[{"internalType":"uint256","name":"marketReferenceCurrencyUnit","type":"uint256"},{"internalType":"int256","name":"marketReferenceCurrencyPriceInUsd","type":"int256"},{"internalType":"int256","name":"networkBaseTokenPriceInUsd","type":"int256"},{"internalType":"uint8","name":"networkBaseTokenPriceDecimals","type":"uint8"}],"internalType":"struct IUiPoolDataProviderV3.BaseCurrencyInfo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILendingPoolAddressesProvider","name":"provider","type":"address"}],"name":"getReservesList","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILendingPoolAddressesProvider","name":"provider","type":"address"},{"internalType":"address","name":"user","type":"address"}],"name":"getUserReservesData","outputs":[{"components":[{"internalType":"address","name":"underlyingAsset","type":"address"},{"internalType":"uint256","name":"scaledATokenBalance","type":"uint256"},{"internalType":"bool","name":"usageAsCollateralEnabledOnUser","type":"bool"},{"internalType":"uint256","name":"stableBorrowRate","type":"uint256"},{"internalType":"uint256","name":"scaledVariableDebt","type":"uint256"},{"internalType":"uint256","name":"principalStableDebt","type":"uint256"},{"internalType":"uint256","name":"stableBorrowLastUpdateTimestamp","type":"uint256"}],"internalType":"struct IUiPoolDataProviderV3.UserReserveData[]","name":"","type":"tuple[]"},{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"marketReferenceCurrencyPriceInUsdProxyAggregator","outputs":[{"internalType":"contract IChainlinkAggregator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"networkBaseTokenPriceInUsdProxyAggregator","outputs":[{"internalType":"contract IChainlinkAggregator","name":"","type":"address"}],"stateMutability":"view","type":"function"}]
uniswap_abi = [{"inputs":[{"internalType":"bytes32","name":"previousBlockhash","type":"bytes32"},{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"}]
gmx_reader_abi = [{"inputs":[],"name":"BASIS_POINTS_DIVISOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"POSITION_PROPS_LENGTH","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PRICE_PRECISION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USDG_DECIMALS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IVault","name":"_vault","type":"address"},{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"address","name":"_tokenOut","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IVault","name":"_vault","type":"address"},{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"address","name":"_tokenOut","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"}],"name":"getFeeBasisPoints","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getFees","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address","name":"_weth","type":"address"},{"internalType":"uint256","name":"_usdgAmount","type":"uint256"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getFullVaultTokenInfo","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address","name":"_weth","type":"address"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getFundingRates","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IVault","name":"_vault","type":"address"},{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"address","name":"_tokenOut","type":"address"}],"name":"getMaxAmountIn","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getPairInfo","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address","name":"_account","type":"address"},{"internalType":"address[]","name":"_collateralTokens","type":"address[]"},{"internalType":"address[]","name":"_indexTokens","type":"address[]"},{"internalType":"bool[]","name":"_isLong","type":"bool[]"}],"name":"getPositions","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IVaultPriceFeed","name":"_priceFeed","type":"address"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getPrices","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"address[]","name":"_yieldTrackers","type":"address[]"}],"name":"getStakingInfo","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getTokenBalances","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getTokenBalancesWithSupplies","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_token","type":"address"},{"internalType":"address[]","name":"_excludedAccounts","type":"address[]"}],"name":"getTokenSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_token","type":"address"},{"internalType":"address[]","name":"_accounts","type":"address[]"}],"name":"getTotalBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_yieldTokens","type":"address[]"}],"name":"getTotalStaked","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address","name":"_weth","type":"address"},{"internalType":"uint256","name":"_usdgAmount","type":"uint256"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getVaultTokenInfo","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address","name":"_weth","type":"address"},{"internalType":"uint256","name":"_usdgAmount","type":"uint256"},{"internalType":"address[]","name":"_tokens","type":"address[]"}],"name":"getVaultTokenInfoV2","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"address[]","name":"_vesters","type":"address[]"}],"name":"getVestingInfo","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gov","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"hasMaxGlobalShortSizes","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_hasMaxGlobalShortSizes","type":"bool"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_gov","type":"address"}],"name":"setGov","outputs":[],"stateMutability":"nonpayable","type":"function"}]
snx_exchange_rates_abi = [{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_resolver","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"address","name":"aggregator","type":"address"}],"name":"AggregatorAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"address","name":"aggregator","type":"address"}],"name":"AggregatorRemoved","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"name","type":"bytes32"},{"indexed":False,"internalType":"address","name":"destination","type":"address"}],"name":"CacheUpdated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"newDexPriceAggregator","type":"address"}],"name":"DexPriceAggregatorUpdated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerNominated","type":"event"},{"constant":True,"inputs":[],"name":"CONTRACT_NAME","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"address","name":"aggregatorAddress","type":"address"}],"name":"addAggregator","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"aggregatorKeys","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"aggregatorWarningFlags","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"aggregators","outputs":[{"internalType":"contract AggregatorV2V3Interface","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32[]","name":"currencyKeys","type":"bytes32[]"}],"name":"anyRateIsInvalid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32[]","name":"currencyKeys","type":"bytes32[]"},{"internalType":"uint256[]","name":"roundIds","type":"uint256[]"}],"name":"anyRateIsInvalidAtRound","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"aggregator","type":"address"}],"name":"currenciesUsingAggregator","outputs":[{"internalType":"bytes32[]","name":"currencies","type":"bytes32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"currencyKeyDecimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"dexPriceAggregator","outputs":[{"internalType":"contract IDexPriceAggregator","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"sourceCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes32","name":"destinationCurrencyKey","type":"bytes32"}],"name":"effectiveAtomicValueAndRates","outputs":[{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"systemValue","type":"uint256"},{"internalType":"uint256","name":"systemSourceRate","type":"uint256"},{"internalType":"uint256","name":"systemDestinationRate","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"components":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"address","name":"dexPriceAggregator","type":"address"},{"internalType":"address","name":"atomicEquivalentForDexPricing","type":"address"},{"internalType":"uint256","name":"atomicExchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"atomicTwapWindow","type":"uint256"},{"internalType":"uint256","name":"atomicMaxVolumePerBlock","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityConsiderationWindow","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityUpdateThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"exchangeMaxDynamicFee","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeRounds","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeWeightDecay","type":"uint256"}],"internalType":"struct IDirectIntegrationManager.ParameterIntegrationSettings","name":"sourceSettings","type":"tuple"},{"internalType":"uint256","name":"sourceAmount","type":"uint256"},{"components":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"address","name":"dexPriceAggregator","type":"address"},{"internalType":"address","name":"atomicEquivalentForDexPricing","type":"address"},{"internalType":"uint256","name":"atomicExchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"atomicTwapWindow","type":"uint256"},{"internalType":"uint256","name":"atomicMaxVolumePerBlock","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityConsiderationWindow","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityUpdateThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"exchangeMaxDynamicFee","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeRounds","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeWeightDecay","type":"uint256"}],"internalType":"struct IDirectIntegrationManager.ParameterIntegrationSettings","name":"destinationSettings","type":"tuple"},{"components":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"address","name":"dexPriceAggregator","type":"address"},{"internalType":"address","name":"atomicEquivalentForDexPricing","type":"address"},{"internalType":"uint256","name":"atomicExchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"atomicTwapWindow","type":"uint256"},{"internalType":"uint256","name":"atomicMaxVolumePerBlock","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityConsiderationWindow","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityUpdateThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"exchangeMaxDynamicFee","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeRounds","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeWeightDecay","type":"uint256"}],"internalType":"struct IDirectIntegrationManager.ParameterIntegrationSettings","name":"usdSettings","type":"tuple"}],"name":"effectiveAtomicValueAndRates","outputs":[{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"systemValue","type":"uint256"},{"internalType":"uint256","name":"systemSourceRate","type":"uint256"},{"internalType":"uint256","name":"systemDestinationRate","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"sourceCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"sourceAmount","type":"uint256"},{"internalType":"bytes32","name":"destinationCurrencyKey","type":"bytes32"}],"name":"effectiveValue","outputs":[{"internalType":"uint256","name":"value","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"sourceCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"sourceAmount","type":"uint256"},{"internalType":"bytes32","name":"destinationCurrencyKey","type":"bytes32"}],"name":"effectiveValueAndRates","outputs":[{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"sourceRate","type":"uint256"},{"internalType":"uint256","name":"destinationRate","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"sourceCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"sourceAmount","type":"uint256"},{"internalType":"bytes32","name":"destinationCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"roundIdForSrc","type":"uint256"},{"internalType":"uint256","name":"roundIdForDest","type":"uint256"}],"name":"effectiveValueAndRatesAtRound","outputs":[{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"sourceRate","type":"uint256"},{"internalType":"uint256","name":"destinationRate","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"getCurrentRoundId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"uint256","name":"startingRoundId","type":"uint256"},{"internalType":"uint256","name":"startingTimestamp","type":"uint256"},{"internalType":"uint256","name":"timediff","type":"uint256"}],"name":"getLastRoundIdBeforeElapsedSecs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"isResolverCached","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"lastRateUpdateTimes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32[]","name":"currencyKeys","type":"bytes32[]"}],"name":"lastRateUpdateTimesForCurrencies","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"nominateNewOwner","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"nominatedOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"rateAndInvalid","outputs":[{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"bool","name":"isInvalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"uint256","name":"roundId","type":"uint256"}],"name":"rateAndTimestampAtRound","outputs":[{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"rateAndUpdatedTime","outputs":[{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"uint256","name":"time","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"rateForCurrency","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"rateIsFlagged","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"rateIsInvalid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"rateIsStale","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"rateStalePeriod","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"rateWithSafetyChecks","outputs":[{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"bool","name":"broken","type":"bool"},{"internalType":"bool","name":"staleOrInvalid","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32[]","name":"currencyKeys","type":"bytes32[]"}],"name":"ratesAndInvalidForCurrencies","outputs":[{"internalType":"uint256[]","name":"rates","type":"uint256[]"},{"internalType":"bool","name":"anyRateInvalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"uint256","name":"numRounds","type":"uint256"},{"internalType":"uint256","name":"roundId","type":"uint256"}],"name":"ratesAndUpdatedTimeForCurrencyLastNRounds","outputs":[{"internalType":"uint256[]","name":"rates","type":"uint256[]"},{"internalType":"uint256[]","name":"times","type":"uint256[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32[]","name":"currencyKeys","type":"bytes32[]"}],"name":"ratesForCurrencies","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"rebuildCache","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"removeAggregator","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"resolver","outputs":[{"internalType":"contract AddressResolver","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"resolverAddressesRequired","outputs":[{"internalType":"bytes32[]","name":"addresses","type":"bytes32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"contract IDexPriceAggregator","name":"_dexPriceAggregator","type":"address"}],"name":"setDexPriceAggregator","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"synthTooVolatileForAtomicExchange","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"components":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"address","name":"dexPriceAggregator","type":"address"},{"internalType":"address","name":"atomicEquivalentForDexPricing","type":"address"},{"internalType":"uint256","name":"atomicExchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"atomicTwapWindow","type":"uint256"},{"internalType":"uint256","name":"atomicMaxVolumePerBlock","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityConsiderationWindow","type":"uint256"},{"internalType":"uint256","name":"atomicVolatilityUpdateThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeFeeRate","type":"uint256"},{"internalType":"uint256","name":"exchangeMaxDynamicFee","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeRounds","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeThreshold","type":"uint256"},{"internalType":"uint256","name":"exchangeDynamicFeeWeightDecay","type":"uint256"}],"internalType":"struct IDirectIntegrationManager.ParameterIntegrationSettings","name":"settings","type":"tuple"}],"name":"synthTooVolatileForAtomicExchange","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"}]
transferMarginETH_abi = [{"inputs":[{"internalType":"address","name":"_resolver","type":"address"},{"internalType":"bytes32","name":"_baseAsset","type":"bytes32"},{"internalType":"bytes32","name":"_marketKey","type":"bytes32"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"name","type":"bytes32"},{"indexed":False,"internalType":"address","name":"destination","type":"address"}],"name":"CacheUpdated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"int256","name":"funding","type":"int256"},{"indexed":False,"internalType":"uint256","name":"index","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"FundingRecomputed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"trackingCode","type":"bytes32"},{"indexed":False,"internalType":"bytes32","name":"baseAsset","type":"bytes32"},{"indexed":False,"internalType":"bytes32","name":"marketKey","type":"bytes32"},{"indexed":False,"internalType":"int256","name":"sizeDelta","type":"int256"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"FuturesTracking","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"int256","name":"marginDelta","type":"int256"}],"name":"MarginTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"uint256","name":"currentRoundId","type":"uint256"},{"indexed":False,"internalType":"int256","name":"sizeDelta","type":"int256"},{"indexed":False,"internalType":"uint256","name":"targetRoundId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"commitDeposit","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"keeperDeposit","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"NextPriceOrderRemoved","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"int256","name":"sizeDelta","type":"int256"},{"indexed":False,"internalType":"uint256","name":"targetRoundId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"commitDeposit","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"keeperDeposit","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"NextPriceOrderSubmitted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"liquidator","type":"address"},{"indexed":False,"internalType":"int256","name":"size","type":"int256"},{"indexed":False,"internalType":"uint256","name":"price","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"PositionLiquidated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"uint256","name":"margin","type":"uint256"},{"indexed":False,"internalType":"int256","name":"size","type":"int256"},{"indexed":False,"internalType":"int256","name":"tradeSize","type":"int256"},{"indexed":False,"internalType":"uint256","name":"lastPrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"fundingIndex","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"PositionModified","type":"event"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"accessibleMargin","outputs":[{"internalType":"uint256","name":"marginAccessible","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"accruedFunding","outputs":[{"internalType":"int256","name":"funding","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"assetPrice","outputs":[{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"baseAsset","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"canLiquidate","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"cancelNextPriceOrder","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"closePosition","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"closePositionWithTracking","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"currentFundingRate","outputs":[{"internalType":"int256","name":"","type":"int256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"executeNextPriceOrder","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"fundingLastRecomputed","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"fundingSequence","outputs":[{"internalType":"int128","name":"","type":"int128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"fundingSequenceLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"isResolverCached","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"liquidatePosition","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"liquidationFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"liquidationPrice","outputs":[{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketDebt","outputs":[{"internalType":"uint256","name":"debt","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketKey","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketSize","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketSizes","outputs":[{"internalType":"uint256","name":"long","type":"uint256"},{"internalType":"uint256","name":"short","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketSkew","outputs":[{"internalType":"int128","name":"","type":"int128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"}],"name":"modifyPosition","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"},{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"modifyPositionWithTracking","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nextPriceOrders","outputs":[{"internalType":"int128","name":"sizeDelta","type":"int128"},{"internalType":"uint128","name":"targetRoundId","type":"uint128"},{"internalType":"uint128","name":"commitDeposit","type":"uint128"},{"internalType":"uint128","name":"keeperDeposit","type":"uint128"},{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"notionalValue","outputs":[{"internalType":"int256","name":"value","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"}],"name":"orderFee","outputs":[{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"positions","outputs":[{"internalType":"uint64","name":"id","type":"uint64"},{"internalType":"uint64","name":"lastFundingIndex","type":"uint64"},{"internalType":"uint128","name":"margin","type":"uint128"},{"internalType":"uint128","name":"lastPrice","type":"uint128"},{"internalType":"int128","name":"size","type":"int128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"},{"internalType":"address","name":"sender","type":"address"}],"name":"postTradeDetails","outputs":[{"internalType":"uint256","name":"margin","type":"uint256"},{"internalType":"int256","name":"size","type":"int256"},{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"uint256","name":"liqPrice","type":"uint256"},{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"enum IFuturesMarketBaseTypes.Status","name":"status","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"profitLoss","outputs":[{"internalType":"int256","name":"pnl","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"rebuildCache","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"recomputeFunding","outputs":[{"internalType":"uint256","name":"lastIndex","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"remainingMargin","outputs":[{"internalType":"uint256","name":"marginRemaining","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"resolver","outputs":[{"internalType":"contract AddressResolver","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"resolverAddressesRequired","outputs":[{"internalType":"bytes32[]","name":"addresses","type":"bytes32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"}],"name":"submitNextPriceOrder","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"},{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"submitNextPriceOrderWithTracking","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"marginDelta","type":"int256"}],"name":"transferMargin","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"unrecordedFunding","outputs":[{"internalType":"int256","name":"funding","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"withdrawAllMargin","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}]
futuresMarketEth_abi = [{"inputs":[{"internalType":"address","name":"_resolver","type":"address"},{"internalType":"bytes32","name":"_baseAsset","type":"bytes32"},{"internalType":"bytes32","name":"_marketKey","type":"bytes32"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"name","type":"bytes32"},{"indexed":False,"internalType":"address","name":"destination","type":"address"}],"name":"CacheUpdated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"int256","name":"funding","type":"int256"},{"indexed":False,"internalType":"uint256","name":"index","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"FundingRecomputed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"trackingCode","type":"bytes32"},{"indexed":False,"internalType":"bytes32","name":"baseAsset","type":"bytes32"},{"indexed":False,"internalType":"bytes32","name":"marketKey","type":"bytes32"},{"indexed":False,"internalType":"int256","name":"sizeDelta","type":"int256"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"FuturesTracking","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"int256","name":"marginDelta","type":"int256"}],"name":"MarginTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"uint256","name":"currentRoundId","type":"uint256"},{"indexed":False,"internalType":"int256","name":"sizeDelta","type":"int256"},{"indexed":False,"internalType":"uint256","name":"targetRoundId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"commitDeposit","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"keeperDeposit","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"NextPriceOrderRemoved","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"int256","name":"sizeDelta","type":"int256"},{"indexed":False,"internalType":"uint256","name":"targetRoundId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"commitDeposit","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"keeperDeposit","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"NextPriceOrderSubmitted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"liquidator","type":"address"},{"indexed":False,"internalType":"int256","name":"size","type":"int256"},{"indexed":False,"internalType":"uint256","name":"price","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"PositionLiquidated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"uint256","name":"margin","type":"uint256"},{"indexed":False,"internalType":"int256","name":"size","type":"int256"},{"indexed":False,"internalType":"int256","name":"tradeSize","type":"int256"},{"indexed":False,"internalType":"uint256","name":"lastPrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"fundingIndex","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"PositionModified","type":"event"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"accessibleMargin","outputs":[{"internalType":"uint256","name":"marginAccessible","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"accruedFunding","outputs":[{"internalType":"int256","name":"funding","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"assetPrice","outputs":[{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"baseAsset","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"canLiquidate","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"cancelNextPriceOrder","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"closePosition","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"closePositionWithTracking","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"currentFundingRate","outputs":[{"internalType":"int256","name":"","type":"int256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"executeNextPriceOrder","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"fundingLastRecomputed","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"fundingSequence","outputs":[{"internalType":"int128","name":"","type":"int128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"fundingSequenceLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"isResolverCached","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"liquidatePosition","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"liquidationFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"liquidationPrice","outputs":[{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketDebt","outputs":[{"internalType":"uint256","name":"debt","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketKey","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketSize","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketSizes","outputs":[{"internalType":"uint256","name":"long","type":"uint256"},{"internalType":"uint256","name":"short","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"marketSkew","outputs":[{"internalType":"int128","name":"","type":"int128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"}],"name":"modifyPosition","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"},{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"modifyPositionWithTracking","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nextPriceOrders","outputs":[{"internalType":"int128","name":"sizeDelta","type":"int128"},{"internalType":"uint128","name":"targetRoundId","type":"uint128"},{"internalType":"uint128","name":"commitDeposit","type":"uint128"},{"internalType":"uint128","name":"keeperDeposit","type":"uint128"},{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"notionalValue","outputs":[{"internalType":"int256","name":"value","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"}],"name":"orderFee","outputs":[{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"positions","outputs":[{"internalType":"uint64","name":"id","type":"uint64"},{"internalType":"uint64","name":"lastFundingIndex","type":"uint64"},{"internalType":"uint128","name":"margin","type":"uint128"},{"internalType":"uint128","name":"lastPrice","type":"uint128"},{"internalType":"int128","name":"size","type":"int128"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"},{"internalType":"address","name":"sender","type":"address"}],"name":"postTradeDetails","outputs":[{"internalType":"uint256","name":"margin","type":"uint256"},{"internalType":"int256","name":"size","type":"int256"},{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"uint256","name":"liqPrice","type":"uint256"},{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"enum IFuturesMarketBaseTypes.Status","name":"status","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"profitLoss","outputs":[{"internalType":"int256","name":"pnl","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"rebuildCache","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"recomputeFunding","outputs":[{"internalType":"uint256","name":"lastIndex","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"remainingMargin","outputs":[{"internalType":"uint256","name":"marginRemaining","type":"uint256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"resolver","outputs":[{"internalType":"contract AddressResolver","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"resolverAddressesRequired","outputs":[{"internalType":"bytes32[]","name":"addresses","type":"bytes32[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"}],"name":"submitNextPriceOrder","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"sizeDelta","type":"int256"},{"internalType":"bytes32","name":"trackingCode","type":"bytes32"}],"name":"submitNextPriceOrderWithTracking","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"int256","name":"marginDelta","type":"int256"}],"name":"transferMargin","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"unrecordedFunding","outputs":[{"internalType":"int256","name":"funding","type":"int256"},{"internalType":"bool","name":"invalid","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"withdrawAllMargin","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}]
GMX_router_abi = [{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address","name":"_usdg","type":"address"},{"internalType":"address","name":"_weth","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"address","name":"tokenIn","type":"address"},{"indexed":False,"internalType":"address","name":"tokenOut","type":"address"},{"indexed":False,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"Swap","type":"event"},{"inputs":[{"internalType":"address","name":"_plugin","type":"address"}],"name":"addPlugin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_plugin","type":"address"}],"name":"approvePlugin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"approvedPlugins","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_collateralToken","type":"address"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_collateralDelta","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"decreasePosition","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_collateralDelta","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_price","type":"uint256"},{"internalType":"uint256","name":"_minOut","type":"uint256"}],"name":"decreasePositionAndSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_collateralDelta","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"address payable","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_price","type":"uint256"},{"internalType":"uint256","name":"_minOut","type":"uint256"}],"name":"decreasePositionAndSwapETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_collateralToken","type":"address"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_collateralDelta","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"address payable","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"decreasePositionETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_plugin","type":"address"}],"name":"denyPlugin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"directPoolDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"gov","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"increasePosition","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"increasePositionETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"address","name":"_collateralToken","type":"address"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_collateralDelta","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"address","name":"_receiver","type":"address"}],"name":"pluginDecreasePosition","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"address","name":"_collateralToken","type":"address"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"}],"name":"pluginIncreasePosition","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_account","type":"address"},{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"pluginTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"plugins","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_plugin","type":"address"}],"name":"removePlugin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_gov","type":"address"}],"name":"setGov","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"address","name":"_receiver","type":"address"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"address","name":"_receiver","type":"address"}],"name":"swapETHToTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"address payable","name":"_receiver","type":"address"}],"name":"swapTokensToETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"usdg","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"vault","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"weth","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]
GMX_positon_router_abi = [{"inputs":[{"internalType":"address","name":"_vault","type":"address"},{"internalType":"address","name":"_router","type":"address"},{"internalType":"address","name":"_weth","type":"address"},{"internalType":"address","name":"_shortsTracker","type":"address"},{"internalType":"uint256","name":"_depositFee","type":"uint256"},{"internalType":"uint256","name":"_minExecutionFee","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"callbackTarget","type":"address"},{"indexed":False,"internalType":"bool","name":"success","type":"bool"}],"name":"Callback","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"address[]","name":"path","type":"address[]"},{"indexed":False,"internalType":"address","name":"indexToken","type":"address"},{"indexed":False,"internalType":"uint256","name":"collateralDelta","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"bool","name":"isLong","type":"bool"},{"indexed":False,"internalType":"address","name":"receiver","type":"address"},{"indexed":False,"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minOut","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"executionFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockGap","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timeGap","type":"uint256"}],"name":"CancelDecreasePosition","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"address[]","name":"path","type":"address[]"},{"indexed":False,"internalType":"address","name":"indexToken","type":"address"},{"indexed":False,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minOut","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"bool","name":"isLong","type":"bool"},{"indexed":False,"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"executionFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockGap","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timeGap","type":"uint256"}],"name":"CancelIncreasePosition","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"address[]","name":"path","type":"address[]"},{"indexed":False,"internalType":"address","name":"indexToken","type":"address"},{"indexed":False,"internalType":"uint256","name":"collateralDelta","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"bool","name":"isLong","type":"bool"},{"indexed":False,"internalType":"address","name":"receiver","type":"address"},{"indexed":False,"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minOut","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"executionFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"index","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"queueIndex","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockNumber","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockTime","type":"uint256"}],"name":"CreateDecreasePosition","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"address[]","name":"path","type":"address[]"},{"indexed":False,"internalType":"address","name":"indexToken","type":"address"},{"indexed":False,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minOut","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"bool","name":"isLong","type":"bool"},{"indexed":False,"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"executionFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"index","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"queueIndex","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockNumber","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockTime","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"gasPrice","type":"uint256"}],"name":"CreateIncreasePosition","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"marginFeeBasisPoints","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"referralCode","type":"bytes32"},{"indexed":False,"internalType":"address","name":"referrer","type":"address"}],"name":"DecreasePositionReferral","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"address[]","name":"path","type":"address[]"},{"indexed":False,"internalType":"address","name":"indexToken","type":"address"},{"indexed":False,"internalType":"uint256","name":"collateralDelta","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"bool","name":"isLong","type":"bool"},{"indexed":False,"internalType":"address","name":"receiver","type":"address"},{"indexed":False,"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minOut","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"executionFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockGap","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timeGap","type":"uint256"}],"name":"ExecuteDecreasePosition","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"address[]","name":"path","type":"address[]"},{"indexed":False,"internalType":"address","name":"indexToken","type":"address"},{"indexed":False,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minOut","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"bool","name":"isLong","type":"bool"},{"indexed":False,"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"executionFee","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"blockGap","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"timeGap","type":"uint256"}],"name":"ExecuteIncreasePosition","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"marginFeeBasisPoints","type":"uint256"},{"indexed":False,"internalType":"bytes32","name":"referralCode","type":"bytes32"},{"indexed":False,"internalType":"address","name":"referrer","type":"address"}],"name":"IncreasePositionReferral","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"admin","type":"address"}],"name":"SetAdmin","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"callbackGasLimit","type":"uint256"}],"name":"SetCallbackGasLimit","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"minBlockDelayKeeper","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minTimeDelayPublic","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"maxTimeDelay","type":"uint256"}],"name":"SetDelayValues","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"depositFee","type":"uint256"}],"name":"SetDepositFee","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"increasePositionBufferBps","type":"uint256"}],"name":"SetIncreasePositionBufferBps","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bool","name":"isLeverageEnabled","type":"bool"}],"name":"SetIsLeverageEnabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address[]","name":"tokens","type":"address[]"},{"indexed":False,"internalType":"uint256[]","name":"longSizes","type":"uint256[]"},{"indexed":False,"internalType":"uint256[]","name":"shortSizes","type":"uint256[]"}],"name":"SetMaxGlobalSizes","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"minExecutionFee","type":"uint256"}],"name":"SetMinExecutionFee","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bool","name":"isActive","type":"bool"}],"name":"SetPositionKeeper","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"referralStorage","type":"address"}],"name":"SetReferralStorage","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"increasePositionRequestKeysStart","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"decreasePositionRequestKeysStart","type":"uint256"}],"name":"SetRequestKeysStartValues","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"token","type":"address"},{"indexed":False,"internalType":"address","name":"receiver","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawFees","type":"event"},{"inputs":[],"name":"BASIS_POINTS_DIVISOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"callbackGasLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_key","type":"bytes32"},{"internalType":"address payable","name":"_executionFeeReceiver","type":"address"}],"name":"cancelDecreasePosition","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_key","type":"bytes32"},{"internalType":"address payable","name":"_executionFeeReceiver","type":"address"}],"name":"cancelIncreasePosition","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_collateralDelta","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"address","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_acceptablePrice","type":"uint256"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"uint256","name":"_executionFee","type":"uint256"},{"internalType":"bool","name":"_withdrawETH","type":"bool"},{"internalType":"address","name":"_callbackTarget","type":"address"}],"name":"createDecreasePosition","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"uint256","name":"_acceptablePrice","type":"uint256"},{"internalType":"uint256","name":"_executionFee","type":"uint256"},{"internalType":"bytes32","name":"_referralCode","type":"bytes32"},{"internalType":"address","name":"_callbackTarget","type":"address"}],"name":"createIncreasePosition","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_path","type":"address[]"},{"internalType":"address","name":"_indexToken","type":"address"},{"internalType":"uint256","name":"_minOut","type":"uint256"},{"internalType":"uint256","name":"_sizeDelta","type":"uint256"},{"internalType":"bool","name":"_isLong","type":"bool"},{"internalType":"uint256","name":"_acceptablePrice","type":"uint256"},{"internalType":"uint256","name":"_executionFee","type":"uint256"},{"internalType":"bytes32","name":"_referralCode","type":"bytes32"},{"internalType":"address","name":"_callbackTarget","type":"address"}],"name":"createIncreasePositionETH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"decreasePositionRequestKeys","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decreasePositionRequestKeysStart","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"decreasePositionRequests","outputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"indexToken","type":"address"},{"internalType":"uint256","name":"collateralDelta","type":"uint256"},{"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"internalType":"bool","name":"isLong","type":"bool"},{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"internalType":"uint256","name":"minOut","type":"uint256"},{"internalType":"uint256","name":"executionFee","type":"uint256"},{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"uint256","name":"blockTime","type":"uint256"},{"internalType":"bool","name":"withdrawETH","type":"bool"},{"internalType":"address","name":"callbackTarget","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"decreasePositionsIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_key","type":"bytes32"},{"internalType":"address payable","name":"_executionFeeReceiver","type":"address"}],"name":"executeDecreasePosition","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_endIndex","type":"uint256"},{"internalType":"address payable","name":"_executionFeeReceiver","type":"address"}],"name":"executeDecreasePositions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_key","type":"bytes32"},{"internalType":"address payable","name":"_executionFeeReceiver","type":"address"}],"name":"executeIncreasePosition","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_endIndex","type":"uint256"},{"internalType":"address payable","name":"_executionFeeReceiver","type":"address"}],"name":"executeIncreasePositions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"feeReserves","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_key","type":"bytes32"}],"name":"getDecreasePositionRequestPath","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_key","type":"bytes32"}],"name":"getIncreasePositionRequestPath","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getRequestKey","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"getRequestQueueLengths","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gov","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"increasePositionBufferBps","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"increasePositionRequestKeys","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"increasePositionRequestKeysStart","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"increasePositionRequests","outputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"indexToken","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"minOut","type":"uint256"},{"internalType":"uint256","name":"sizeDelta","type":"uint256"},{"internalType":"bool","name":"isLong","type":"bool"},{"internalType":"uint256","name":"acceptablePrice","type":"uint256"},{"internalType":"uint256","name":"executionFee","type":"uint256"},{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"uint256","name":"blockTime","type":"uint256"},{"internalType":"bool","name":"hasCollateralInETH","type":"bool"},{"internalType":"address","name":"callbackTarget","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"increasePositionsIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isLeverageEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isPositionKeeper","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"maxGlobalLongSizes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"maxGlobalShortSizes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxTimeDelay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minBlockDelayKeeper","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minExecutionFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minTimeDelayPublic","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"referralStorage","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"router","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address payable","name":"_receiver","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"sendValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_admin","type":"address"}],"name":"setAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_callbackGasLimit","type":"uint256"}],"name":"setCallbackGasLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_minBlockDelayKeeper","type":"uint256"},{"internalType":"uint256","name":"_minTimeDelayPublic","type":"uint256"},{"internalType":"uint256","name":"_maxTimeDelay","type":"uint256"}],"name":"setDelayValues","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_depositFee","type":"uint256"}],"name":"setDepositFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_gov","type":"address"}],"name":"setGov","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_increasePositionBufferBps","type":"uint256"}],"name":"setIncreasePositionBufferBps","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_isLeverageEnabled","type":"bool"}],"name":"setIsLeverageEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_tokens","type":"address[]"},{"internalType":"uint256[]","name":"_longSizes","type":"uint256[]"},{"internalType":"uint256[]","name":"_shortSizes","type":"uint256[]"}],"name":"setMaxGlobalSizes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_minExecutionFee","type":"uint256"}],"name":"setMinExecutionFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bool","name":"_isActive","type":"bool"}],"name":"setPositionKeeper","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_referralStorage","type":"address"}],"name":"setReferralStorage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_increasePositionRequestKeysStart","type":"uint256"},{"internalType":"uint256","name":"_decreasePositionRequestKeysStart","type":"uint256"}],"name":"setRequestKeysStartValues","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"shortsTracker","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"vault","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"weth","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_receiver","type":"address"}],"name":"withdrawFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
