function getChainLinkData(web3, listOfAssets) {
    // Initialize BTC/USD and ETH/USD contracts since they may be used several times
    const priceFeedBTC = new web3.eth.Contract(aggregatorV3InterfaceABI, "0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c");
    const priceFeedETH = new web3.eth.Contract(aggregatorV3InterfaceABI, "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419");

    for (const [address, dict] of Object.entries(listOfAssets)) {
        if (dict.chainlink_address_usd === undefined) {
            if (dict.chainlink_address_eth === undefined) {
                //use BTC price feed
                const priceFeed = new web3.eth.Contract(aggregatorV3InterfaceABI, dict.chainlink_address_btc)
                priceFeed.methods.latestRoundData().call().then((roundData) => {
                    const btc_value = roundData.answer / 10**8;
                    priceFeedBTC.methods.latestRoundData().call().then((roundData) => {
                        dict.valueUSD = roundData.answer*btc_value / 10**8
                        // console.log(dict.name)
                        // console.log("BTC value of above: ", btc_value)
                        // console.log("USD value of above: ", dict.valueUSD)
                    })
                })
            }
            else {
                //use ETH price feed
                const priceFeed = new web3.eth.Contract(aggregatorV3InterfaceABI, dict.chainlink_address_eth)
                priceFeed.methods.latestRoundData().call().then((roundData) => {
                    const eth_value = roundData.answer / 10**18;
                    priceFeedETH.methods.latestRoundData().call().then((roundData) => {
                        dict.valueUSD = roundData.answer*eth_value / 10**8
                        // console.log(dict.name)
                        // console.log("ETH value of above: ", eth_value)
                        // console.log("USD value of above: ", dict.valueUSD)
                    })
                })
            }
        }
        else {
            //use USD price feed
            const priceFeed = new web3.eth.Contract(aggregatorV3InterfaceABI, dict.chainlink_address_usd)
            priceFeed.methods.latestRoundData().call().then((roundData) => {
                dict.valueUSD = roundData.answer / 10**8
                //console.log(dict.name)
                //console.log("Value of above in USD: ", dict.valueUSD) //USD prices returned with 8 decimals                
            })
        }
    }
}

async function getBorrowLendAddresses(listOfAssets, lendingPool) {
  for (const [address, dict] of Object.entries(listOfAssets)) {
    reserveData = await lendingPool.methods.getReserveData(address).call()
    dict.aTokenAddress = reserveData.aTokenAddress;
    dict.stableDebtTokenAddress = reserveData.stableDebtTokenAddress;
    dict.variableDebtTokenAddress = reserveData.variableDebtTokenAddress;
    dict.liquidityIndex = reserveData.liquidityIndex;

    const RAY = 10**27 // 10 to the power 27
    const SECONDS_PER_YEAR = 31536000 
    const lendAPR = reserveData.currentLiquidityRate / RAY
    dict.lendAPY = (((1 + (lendAPR / SECONDS_PER_YEAR)) ** SECONDS_PER_YEAR) - 1)*100
    const stableDebtAPR = reserveData.currentStableBorrowRate / RAY;
    dict.stableDebtAPY = (((1 + (stableDebtAPR / SECONDS_PER_YEAR)) ** SECONDS_PER_YEAR) - 1)*100
    const variableDebtAPR = reserveData.currentVariableBorrowRate / RAY;
    dict.variableDebtAPY = (((1 + (variableDebtAPR / SECONDS_PER_YEAR)) ** SECONDS_PER_YEAR) - 1)*100
  }
}


const aggregatorV3InterfaceABI = [
    {
      inputs: [],
      name: "decimals",
      outputs: [{ internalType: "uint8", name: "", type: "uint8" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [],
      name: "description",
      outputs: [{ internalType: "string", name: "", type: "string" }],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [{ internalType: "uint80", name: "_roundId", type: "uint80" }],
      name: "getRoundData",
      outputs: [
        { internalType: "uint80", name: "roundId", type: "uint80" },
        { internalType: "int256", name: "answer", type: "int256" },
        { internalType: "uint256", name: "startedAt", type: "uint256" },
        { internalType: "uint256", name: "updatedAt", type: "uint256" },
        { internalType: "uint80", name: "answeredInRound", type: "uint80" },
      ],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [],
      name: "latestRoundData",
      outputs: [
        { internalType: "uint80", name: "roundId", type: "uint80" },
        { internalType: "int256", name: "answer", type: "int256" },
        { internalType: "uint256", name: "startedAt", type: "uint256" },
        { internalType: "uint256", name: "updatedAt", type: "uint256" },
        { internalType: "uint80", name: "answeredInRound", type: "uint80" },
      ],
      stateMutability: "view",
      type: "function",
    },
    {
      inputs: [],
      name: "version",
      outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
      stateMutability: "view",
      type: "function",
    },
  ]

