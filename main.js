const provider = "" //node provider
web3 = new Web3(new Web3.providers.HttpProvider(provider)) //instatiate web3 object

const aaveGoerliDai_address = "0x75Ab5AB1Eef154C0352Fc31D2428Cef80C7F8B33" //goerli chain address for Dai tokens used by Aave

const dai_contract = new web3.eth.Contract(erc20_abi, aaveGoerliDai_address)

const BN = web3.utils.BN //BigNumber library

const connectButton = document.getElementById("connectButton");
const walletID = document.getElementById("walletID");
const reloadButton = document.getElementById("reloadButton");
const installAlert = document.getElementById("installAlert");
const mobileDeviceWarning = document.getElementById("mobileDeviceWarning");
const depositButton = document.getElementById("depositButton")
const depositAmount = document.getElementById("depositAmount")
const borrowButton = document.getElementById("borrowButton")
const borrowAmount = document.getElementById("borrowAmount")

const startLoading = () => {
  connectButton.classList.add("loadingButton");
};

const stopLoading = () => {
  const timeout = setTimeout(() => {
    connectButton.classList.remove("loadingButton");
    clearTimeout(timeout);
  }, 300);
};

const isMobile = () => {
  let check = false;

  (function (a) {
    if (
      /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(
        a
      ) ||
      /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(
        a.substr(0, 4)
      )
    )
      check = true;
  })(navigator.userAgent || navigator.vendor || window.opera);

  return check;
};

connectButton.addEventListener("click", () => {
  if (typeof window.ethereum !== "undefined") {
    startLoading();

    ethereum
      .request({ method: "eth_requestAccounts" })
      .then((accounts) => {
        const account = accounts[0];

        walletID.innerHTML = `Wallet connected: <span>${account}</span>`;

        stopLoading();
      })
      .catch((error) => {
        console.log(error, error.code);

        alert(error.code);
        stopLoading();
      });
  } else {
    if (isMobile()) {
      mobileDeviceWarning.classList.add("show");
    } else {
      window.open("https://metamask.io/download/", "_blank");
      installAlert.classList.add("show");
    }
  }
});

reloadButton.addEventListener("click", () => {
  window.location.reload();
});

//Interacing with our Aave functions:
//require('./borrowLend') //import our js file with our methods

depositButton.addEventListener("click", () => {
    console.log("Deposit Button Clicked");

    //const amount = new BN(10).pow(BN(19))
    const amount = new BN(depositAmount.value).mul(BN(10).pow(BN(18))) //raise it to 19th power so that we're dealing with whole number dai

    console.log("amount = " + amount)

    approveAndDepositAave(amount);
});

borrowButton.addEventListener("click", () => {
  console.log("Borrow Button Clicked");

  const amount = new BN(borrowAmount.value).mul(BN(10).pow(BN(18))) //raise it to 19th power so that we're dealing with whole number dai

  console.log("amount = " + amount)

  borrowAave(amount);
});

repayButton.addEventListener("click", () => {
  console.log("Repay Button Clicked");
  const amount = new BN(repayAmount.value).mul(BN(10).pow(BN(18))) //raise it to 19th power so that we're dealing with whole number dai

  console.log("amount = " + amount)

  approveAndRepayAave(amount);
});

withdrawButton.addEventListener("click", () => {
  console.log("Withdraw Button Clicked");

  const amount = new BN(withdrawAmount.value).mul(BN(10).pow(BN(18))) //raise it to 19th power so that we're dealing with whole number dai

  console.log("amount = " + amount)

  withdrawAave(amount);
});

async function approveAndRepayAave(amount) {
  const poolAddress = await get_goerli_lending_pool(web3) 
  await approveAave(amount, poolAddress)
  repayAave(amount, poolAddress)
}

async function approveAndDepositAave(amount) {
  const poolAddress = await get_goerli_lending_pool(web3) 
  await approveAave(amount, poolAddress)
  depositAave(amount, poolAddress)
}

async function approveAave(amount, poolAddress) {
    //const poolAddress = await get_goerli_lending_pool(web3) 
    //const gasPrice = await web3.eth.getGasPrice()
    const data = dai_contract.methods.approve(poolAddress, amount).encodeABI()

    //create a transaction to send to the blockchain for approving the funds
    const transactionParameters = {
      to: aaveGoerliDai_address,
      from: ethereum.selectedAddress,
      data: data,
    }
    ethereum.request({ 
        method: "eth_sendTransaction",
        params: [transactionParameters],
    })
}

async function depositAave(amount, poolAddress) {
  //const gasPrice = await web3.eth.getGasPrice()
  const lendCon = new web3.eth.Contract(lending_pool_abi,poolAddress)
  const data = lendCon.methods.deposit(aaveGoerliDai_address, amount, ethereum.selectedAddress, 0).encodeABI()
  
  const transactionParameters = {
    from: ethereum.selectedAddress,
    to: poolAddress,
    data: data,
  }

  ethereum.request({ 
    method: "eth_sendTransaction",
    params: [transactionParameters],
  })
}

async function borrowAave(amount) {
  const poolAddress = await get_goerli_lending_pool(web3) 
  var isChecked = document.getElementById("borrowRateToggle").checked;
  var stableRate;
  if (isChecked === false) {
    stableRate = 2 //variable rate
  }
  else {
    stableRate = 1 //stable rate
  }

  const lendCon = new web3.eth.Contract(lending_pool_abi,poolAddress)
  const data = lendCon.methods.borrow(aaveGoerliDai_address, amount, stableRate, 0, ethereum.selectedAddress).encodeABI()

  const transactionParameters = {
    from: ethereum.selectedAddress,
    to: poolAddress,
    data: data,
  }

  ethereum.request({ 
    method: "eth_sendTransaction",
    params: [transactionParameters],
  })
}

async function repayAave(amount, poolAddress) {
  const lendCon = new web3.eth.Contract(lending_pool_abi,poolAddress)
  var isChecked = document.getElementById("borrowRateToggle").checked;
  var stableRate;
  if (isChecked === false) {
    stableRate = 2 //variable rate
  }
  else {
    stableRate = 1 //stable rate
  }

  const data = lendCon.methods.repay(aaveGoerliDai_address, amount, stableRate, ethereum.selectedAddress).encodeABI()

  const transactionParameters = {
    from: ethereum.selectedAddress,
    to: poolAddress,
    data: data,
  }

  ethereum.request({ 
    method: "eth_sendTransaction",
    params: [transactionParameters],
  })
}

async function withdrawAave(amount) {
  const poolAddress = await get_goerli_lending_pool(web3) 
  const lendCon = new web3.eth.Contract(lending_pool_abi,poolAddress)
  const data = lendCon.methods.withdraw(aaveGoerliDai_address, amount, ethereum.selectedAddress).encodeABI()
  
  const transactionParameters = {
    from: ethereum.selectedAddress,
    to: poolAddress,
    data: data,
  }

  ethereum.request({ 
    method: "eth_sendTransaction",
    params: [transactionParameters],
  })
}

//get lending pool function
async function get_goerli_lending_pool(web3) {
  let lpapaddress = "0x5E52dEc931FFb32f609681B8438A51c675cc232d"
  const lpap = new web3.eth.Contract(lending_pool_addresses_provider_abi,lpapaddress)
  const lendPool = (lpap.methods.getLendingPool().call())
  return lendPool
}