MULTI_SIG_MAINNET_ADDRESS = "0xAE28420C1adC4a3bba95c1e97a2a85b8E1149114"
# MULTI_SIG_ABI = """
# {
#     "anonymous":false,
#     "inputs":[
#         {
#             "indexed":true,
#             "internalType":"bytes32",
#             "name":"approvedHash",
#             "type":"bytes32"
#         },
#         {
#             "indexed":true,
#             "internalType":"address",
#             "name":"owner",
#             "type":"address"
#         }
#     ],
#     "name":"ApproveHash",
#     "type":"event"
# }"""
MULTI_SIG_ABI = """
{
    "anonymous":false,
    "inputs":[
        {
            "indexed":false,
            "internalType":"bytes32",
            "name":"txHash",
            "type":"bytes32"
        },
        {
            "indexed":false,
            "internalType":"uint256",
            "name":"payment",
            "type":"uint256"
        }
    ],
    "name":"ExecutionSuccess",
    "type":"event"
}"""