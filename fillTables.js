function fillTable(listOfAssets, assetsToDisplay) {
  // Get a reference to the table and tbody elements
  var table = document.getElementById("market-borrow-table");
  var tbody = table.getElementsByTagName("tbody")[0];

  // Loop through all assets to display
  assetsToDisplay.forEach(function(assetAddress) {
    asset = listOfAssets[assetAddress];
    // Create a new row and cells
    var newRow = tbody.insertRow();
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);

    // Add style to align first column to left-side and give some padding to images
    cell1.style.cssText +=
    "text-align: left;padding-left: 10px; padding-top:5px; padding-bottom:5px";

    // Get the image of the current asset (if it exists otherwise fallback to generic image)
    var img = new Image();
    var http = new XMLHttpRequest();
    http.open('HEAD', "./asset_images/" + asset.image_src, false);
    http.send();
    if (http.status == 404) {
      img.src = "./asset_images/cold pretzel.png";
    }
    else {
      img.src = "./asset_images/" + asset.image_src;
    }
    
    // Fill the cells with data
    cell1.appendChild(img);
    cell1.innerHTML += "\t" + asset.name;
    cell2.innerHTML = asset.lendAPY.toFixed(2);
    cell3.innerHTML = asset.variableDebtAPY.toFixed(2);
  })
}

function fillAssetList(listOfAssets) {
  listOfAssets["0x0B7a69d978DdA361Db5356D4Bd0206496aFbDD96"] = {
    name: "AAVE",
    image_src: "aave.png",
    chainlink_address_usd: "0xc929ad75B72593967DE83E7F7Cda0493458261D9",
  };

  listOfAssets["0x515614aA3d8f09152b1289848383A260c7D053Ff"] = {
    name: "BAT",
    image_src: "bat.png",
    chainlink_address_eth: "0x0d16d4528239e9ee52fa531af613acdb23d88c94",
  };

  listOfAssets["0xa7c3Bf25FFeA8605B516Cf878B7435fe1768c89b"] = {
    name: "BUSD",
    image_src: "busd.png",
    chainlink_address_usd: "0x833d8eb16d306ed1fbb5d7a2e019e106b960965a",
  };

  listOfAssets["0x75Ab5AB1Eef154C0352Fc31D2428Cef80C7F8B33"] = {
    name: "DAI",
    image_src: "dai.png",
    chainlink_address_usd: "0xAed0c38402a5d19df6E4c03F4E2DceD6e29c1ee9",
  };

  listOfAssets["0x1057DCaa0b66dFBcEc5241fD51F4326C210f201F"] = {
    name: "ENJ",
    image_src: "enj.png",
    chainlink_address_usd: "0x23905c55dc11d609d5d11dc604905779545de9a7",
  };

  listOfAssets["0x54Bc1D59873A5ABde98cf76B6EcF4075ff65d685"] = {
    name: "KNC",
    image_src: "knc.png",
    chainlink_address_usd: "0xf8ff43e991a81e6ec886a3d281a2c6cc19ae70fc",
  };

  listOfAssets["0x7337e7FF9abc45c0e43f130C136a072F4794d40b"] = {
    name: "LINK",
    image_src: "link.png",
    chainlink_address_usd: "0x2c1d072e956AFFC0D435Cb7AC38EF18d24d9127c",
  };

  listOfAssets["0x8d9EAc6f25470EFfD68f0AD22993CB2813c0c9B9"] = {
    name: "MANA",
    image_src: "mana.png",
    chainlink_address_usd: "0x56a4857acbcfe3a66965c251628b1c9f1c408c19",
  };

  listOfAssets["0x90be02599452FBC1a3D47E9EB62895330cfA05Ed"] = {
    name: "MKR",
    image_src: "mkr.png",
    chainlink_address_usd: "0xec1D1B3b0443256cc3860e24a46F108e699484Aa",
  };

  listOfAssets["0x3160F3f3B55eF85d0D27f04A2d74d426c32de842"] = {
    name: "REN",
    image_src: "ren.png",
    chainlink_address_usd: "0x0f59666ede214281e956cb3b2d0d69415aff4a01",
  };

  listOfAssets["0xFc1Ab0379db4B6ad8Bf5Bc1382e108a341E2EaBb"] = {
    name: "SNX",
    image_src: "snx.png",
    chainlink_address_usd: "0xDC3EA94CD0AC27d9A86C180091e7f78C683d3699",
  };

  listOfAssets["0x4e62eB262948671590b8D967BDE048557bdd03eD"] = {
    name: "sUSD",
    image_src: "susd.png",
    chainlink_address_usd: "0xad35bd71b9afe6e4bdc266b345c198eadef9ad94",
  };

  listOfAssets["0xc048C1b6ac47393F073dA2b3d5D1cc43b94891Fd"] = {
    name: "TUSD",
    image_src: "tusd.png",
    chainlink_address_usd: "0xec746eCF986E2927Abd291a2A1716c940100f8Ba",
  };

  listOfAssets["0x981D8AcaF6af3a46785e7741d22fBE81B25Ebf1e"] = {
    name: "UNI",
    image_src: "uni.png",
    chainlink_address_usd: "0x553303d460EE0afB37EdFf9bE42922D8FF63220e",
  };

  listOfAssets["0x9FD21bE27A2B059a288229361E2fA632D8D2d074"] = {
    name: "USDC",
    image_src: "usdc.png",
    chainlink_address_usd: "0x8fFfFfd4AfB6115b954Bd326cbe7B4BA576818f6",
  };

  listOfAssets["0x65E2fe35C30eC218b46266F89847c63c2eDa7Dc7"] = {
    name: "USDT",
    image_src: "usdt.png",
    chainlink_address_usd: "0x3E7d1eAB13ad0104d2750B8863b489D65364e32D",
  };

  listOfAssets["0xf4423F4152966eBb106261740da907662A3569C5"] = {
    name: "WBTC",
    image_src: "wbtc.png",
    chainlink_address_btc: "0xfdFD9C85aD200c506Cf9e21F1FD8dd01932FBB23",
  };

  listOfAssets["0xCCa7d1416518D095E729904aAeA087dBA749A4dC"] = {
    name: "WETH",
    image_src: "eth.png",
    chainlink_address_usd: "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",
  };

  listOfAssets["0x6c260F702B6Bb9AC989DA4B0fcbE7fddF8f749c4"] = {
    name: "YFI",
    image_src: "yfi.png",
    chainlink_address_usd: "0xa027702dbb89fbd58938e4324ac03b58d812b0e1",
  };

  listOfAssets["0xAcFd03DdF9C68015E1943FB02b60c5df56C4CB9e"] = {
    name: "ZRX",
    image_src: "zrx.png",
    chainlink_address_usd: "0x2885d15b8af22648b98b122b22fdf4d2a56c6023",
  };

  listOfAssets["0x45E18E77b15A02a31507e948A546a509A50a2376"] = {
    name: "xSushi",
    image_src: "xsushi.png",
    chainlink_address_usd: "0xcc1f5d9e6956447630d703c8e93b2345c2de3d13",
  };
}

// Create list of all assets to place in table
// function fillAssetList(listOfAssets) {
//   listOfAssets["1INCH"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "1inch.png",
//     testnet_contract: "",
//     mainnet_contract: "0x111111111117dC0aa78b770fA6A738034120C302",
//     chainlink_address_usd: "0xc929ad75B72593967DE83E7F7Cda0493458261D9",
//   };
//   listOfAssets["AAVE"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "aave.png",
//     testnet_contract: "",
//     mainnet_contract: "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
//     chainlink_address_usd: "0x547a514d5e3769680Ce22B2361c10Ea13619e8a9",
// };
//   listOfAssets["APE"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "ape.png",
//     testnet_contract: "",
//     mainnet_contract: "0x4d224452801ACEd8B2F0aebE155379bb5D594381",
//     chainlink_address_usd: "0xD10aBbC76679a20055E167BB80A24ac851b37056",
// };
//   listOfAssets["AVAX"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "avax.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0xFF3EEb22B5E3dE6e705b44749C2559d704923FD7",
// };
//   listOfAssets["cbETH"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "cbeth.png",
//     testnet_contract: "",
//     mainnet_contract: "0xBe9895146f7AF43049ca1c1AE358B0541Ea49704",
//     chainlink_address_usd: null,
//     chainlink_address_eth: "0xF017fcB346A1885194689bA23Eff2fE6fA5C483b",
// };
//   listOfAssets["CRV"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "crv.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0xCd627aA160A6fA45Eb793D19Ef54f5062F20f33f",
// };
//   listOfAssets["DAI"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "dai.png",
//     testnet_contract: "",
//     mainnet_contract: "0x6B175474E89094C44Da98b954EedeAC495271d0F",
//     chainlink_address_usd: "0xAed0c38402a5d19df6E4c03F4E2DceD6e29c1ee9",
// };
//   listOfAssets["DPI"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "dpi.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0xD2A593BF7594aCE1faD597adb697b5645d5edDB2",
// };
//   listOfAssets["ENS"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "ens.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x5C00128d4d1c2F4f652C267d7bcdD7aC99C16E16",
// };
//   listOfAssets["ETH"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "eth.png",
//     testnet_contract: "",
//     mainnet_contract: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
//     chainlink_address_usd: "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"
// };
//   listOfAssets["FRAX"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "frax.png",
//     testnet_contract: "",
//     mainnet_contract: "0x853d955aCEf822Db058eb8505911ED77F175b99e",
//     chainlink_address_usd: "0xB9E1E3A9feFf48998E45Fa90847ed4D467E8BcfD",
// };
//   listOfAssets["GUSD"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "gusd.png",
//     testnet_contract: "",
//     mainnet_contract: "0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd",
//     chainlink_address_usd: "0xa89f5d2365ce98B3cD68012b6f503ab1416245Fc",
// };
//   listOfAssets["LDO"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "ldo.png",
//     testnet_contract: "",
//     mainnet_contract: "0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32",
//     chainlink_address_usd: null,
//     chainlink_address_eth: "0x4e844125952D32AcdF339BE976c98E22F6F318dB",
// };
//   listOfAssets["LINK"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "link.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x2c1d072e956AFFC0D435Cb7AC38EF18d24d9127c",
// };
//   listOfAssets["LUSD"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "lusd.png",
//     testnet_contract: "",
//     mainnet_contract: "0x5f98805A4E8be255a32880FDeC7F6728C6568bA0",
//     chainlink_address_usd: "0x3D7aE7E594f2f2091Ad8798313450130d0Aba3a0",
// };
//   listOfAssets["MATIC"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "matic.png",
//     testnet_contract: "",
//     mainnet_contract: "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0",
//     chainlink_address_usd: "0x7bAC85A8a13A4BcD8abb3eB7d6b4d632c5a57676",
// };
//   listOfAssets["MKR"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "mkr.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0xec1D1B3b0443256cc3860e24a46F108e699484Aa",
// };
//   listOfAssets["rETH"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "reth.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419", // Using just plain ETH/USD for now since no chainlink feed exists
// };
//   listOfAssets["SHIB"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "shib.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: null,
//     chainlink_address_eth: "0x8dD1CD88F43aF196ae478e91b9F5E4Ac69A97C61",
// };
//   listOfAssets["SNX"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "snx.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0xDC3EA94CD0AC27d9A86C180091e7f78C683d3699",
// };
//   listOfAssets["sUSD"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "susd.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: null,
//     chainlink_address_eth: "0x8e0b7e6062272B5eF4524250bFFF8e5Bd3497757",
// };
//   listOfAssets["TUSD"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "tusd.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0xec746eCF986E2927Abd291a2A1716c940100f8Ba",
// };
//   listOfAssets["UNI"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "uni.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x553303d460EE0afB37EdFf9bE42922D8FF63220e",
// };
//   listOfAssets["USDC"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "usdc.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x8fFfFfd4AfB6115b954Bd326cbe7B4BA576818f6",
// };
//   listOfAssets["USDP"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "usdp.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x09023c0DA49Aaf8fc3fA3ADF34C6A7016D38D5e3",
//   };
//   listOfAssets["USDT"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "usdt.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x3E7d1eAB13ad0104d2750B8863b489D65364e32D",
//   };
//   listOfAssets["wBTC"] = {
//     include_mainnet: true,
//     include_testnet: true,
//     image_src: "wbtc.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: null,
//     chainlink_address_eth: null,
//     chainlink_address_btc: "0xfdFD9C85aD200c506Cf9e21F1FD8dd01932FBB23",
//   };
//   listOfAssets["wstETH"] = {
//     include_mainnet: true,
//     include_testnet: false,
//     image_src: "wsteth.png",
//     testnet_contract: "",
//     mainnet_contract: "",
//     chainlink_address_usd: "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419", // Using just plain ETH/USD for now since no chainlink feed exists
//   };
// }
