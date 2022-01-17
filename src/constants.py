MULTI_SIG_MAINNET_ADDRESS = "0xC5aF91F7D10dDe118992ecf536Ed227f276EC60D"
MULTI_SIG_ABI = """
{
    "anonymous":false,
    "inputs":[
        {
            "indexed":true,
            "internalType":"bytes32",
            "name":"approvedHash",
            "type":"bytes32"
        },
        {
            "indexed":true,
            "internalType":"address",
            "name":"owner",
            "type":"address"
        }
    ],
    "name":"ApproveHash",
    "type":"event"
}"""