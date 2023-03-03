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

async function getEthPrice(web3) {
  ethPriceFeedAddress = "0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e"
  const priceFeedETH = new web3.eth.Contract(aggregatorV3InterfaceABI, ethPriceFeedAddress);
  const roundData = await priceFeedETH.methods.latestRoundData().call()
  return roundData.answer / 10**8
}

async function getAssetPrices(web3, lpap, listOfAssets) {
  const priceOracleAddress = await lpap.methods.getPriceOracle().call()
  const priceOracle = new web3.eth.Contract(priceOracleABI, priceOracleAddress)

  const assetAddresses = Object.keys(listOfAssets)
  const prices = await priceOracle.methods.getAssetsPrices(assetAddresses).call()

  for(let i = 0; i < assetAddresses.length; i++) {
    listOfAssets[assetAddresses[i]].priceInETH = prices[i] / 10**18
  }
}


async function fillAssetList(web3, pdp, listOfAssets, userAddress, userLends, userBorrows) {
  //const pdp = new web3.eth.Contract(protocolDataProviderABI, pdpAddress)
  marketAssets = await pdp.methods.getAllReservesTokens().call();
  //Create a hashtable with address as key, and dictionary as value
  marketAssets.forEach((asset) => {
    listOfAssets[asset[1]] = {name: asset[0], image_src: asset[0].toLowerCase() + ".png"}
  })
  //console.log(userAddress === null)

  //add data about each asset to dictionary
  for (const [address, dict] of Object.entries(listOfAssets)) {
    //get aToken and debtToken addresses
    reserveAddresses = await pdp.methods.getReserveTokensAddresses(address).call()
    dict.aTokenAddress = reserveAddresses.aTokenAddress;
    dict.stableDebtTokenAddress = reserveAddresses.stableDebtTokenAddress;
    dict.variableDebtTokenAddress = reserveAddresses.variableDebtTokenAddress;

    //get data on whether borrow/lend/collateral is enabled for this asset
    reserveConfig = await pdp.methods.getReserveConfigurationData(address).call()
    //dict.ltv = reserveConfig.ltv
    //dict.liquidationThreshold = reserveConfig.liquidationThreshold;
    dict.collateralEnabled = reserveConfig.usageAsCollateralEnabled;
    dict.borrowEnabled = reserveConfig.borrowingEnabled;
    dict.stableBorrowEnabled = reserveConfig.stableBorrowRateEnabled;
    dict.isActive = reserveConfig.isActive;

    //get borrow and lend rates
    reserveData = await pdp.methods.getReserveData(address).call()
    //dict.liquidityIndex = reserveData.liquidityIndex;
    dict.availableLiquidity = reserveData.availableLiquidity;
    dict.totalStableDebt = reserveData.totalStableDebt / 10**18;
    dict.totalVariableDebt = reserveData.totalVariableDebt / 10**18;
    const RAY = 10**27 // 10 to the power 27
    const SECONDS_PER_YEAR = 31536000 
    const lendAPR = reserveData.liquidityRate / RAY
    dict.lendAPY = (((1 + (lendAPR / SECONDS_PER_YEAR)) ** SECONDS_PER_YEAR) - 1)*100
    const stableDebtAPR = reserveData.stableBorrowRate / RAY;
    dict.stableDebtAPY = (((1 + (stableDebtAPR / SECONDS_PER_YEAR)) ** SECONDS_PER_YEAR) - 1)*100
    const variableDebtAPR = reserveData.variableBorrowRate / RAY;
    dict.variableDebtAPY = (((1 + (variableDebtAPR / SECONDS_PER_YEAR)) ** SECONDS_PER_YEAR) - 1)*100

    if (userAddress != null) {
      userReserveData = await pdp.methods.getUserReserveData(address, userAddress).call()
      dict.usingAsCollateral = userReserveData.usageAsCollateralEnabled;
      dict.lendValue = userReserveData.currentATokenBalance / 10**18;
      dict.stableDebtValue = userReserveData.currentStableDebt / 10**18;
      dict.variableDebtValue = userReserveData.currentVariableDebt / 10**18;
      if (dict.lendValue > 0) {
        userLends.push(address)
      }
      if (dict.stableDebtValue > 0 || dict.variableDebtValue > 0) {
        userBorrows.push(address)
      }
    }
    else {
      console.log("metamask not connected- can't load user reserve data")
    }
  }
  console.log(listOfAssets);
}

async function getBorrowLendAddresses(listOfAssets, lendingPool, pdp) {
  for (const [address, dict] of Object.entries(listOfAssets)) {
    reserveData = await lendingPool.methods.getReserveData(address).call()
    dict.aTokenAddress = reserveData.aTokenAddress;
    dict.stableDebtTokenAddress = reserveData.stableDebtTokenAddress;
    dict.variableDebtTokenAddress = reserveData.variableDebtTokenAddress;
    dict.liquidityIndex = reserveData.liquidityIndex;

    //Get data from protocol data provider contract
    console.log(await pdp.methods.getAllReservesTokens().call())
    reserveConfigData = await pdp.methods.getReserveConfigurationData(address).call()
    console.log(reserveConfigData)

    //Determine if borrowing and stable borrowing are enabled
    reserveDataBits = parseInt(reserveData.configuration).toString(2)
    reserveDataBits = reserveDataBits.split('').reverse().join("")
    if (reserveDataBits.slice(58,59) === "1") {
      dict.borrowEnabled = true;
    }
    else {
      dict.borrowEnabled = false;
    }
    if (reserveDataBits.slice(59,60) === "1") {
      dict.stableBorrowEnabled = true;
    }
    else {
      dict.stableBorrowEnabled = false;
    }
    if (dict.name === "AAVE") {
      //console.log(dict)
      //console.log(reserveDataBits)
      //console.log(reserveDataBits.slice(56,58))
      //console.log(reserveDataBits.slice(58,59))
    }
    if (dict.name === "DAI") {
      //console.log(dict)
      //console.log(reserveDataBits)
      //console.log(reserveDataBits.slice(56,58))
      //console.log(reserveDataBits.slice(58,59))
    }

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

