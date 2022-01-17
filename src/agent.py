import forta_agent
from forta_agent import Finding, FindingType, FindingSeverity
from src.constants import MULTI_SIG_MAINNET_ADDRESS, MULTI_SIG_ABI

def handle_transaction(transaction_event: forta_agent.transaction_event):
    findings = []

    # filter transaction event in the multi sig wallet

    events  = transaction_event.filter_log(MULTI_SIG_ABI, MULTI_SIG_MAINNET_ADDRESS)

    for event in events:
        msg_hash = event.get('args', {}).get('approvedHash', None)
        msg_hash = msg_hash if msg_hash else 'UNKNOW_HASH'
        executor = event.get('args', {}).get('owner', None)
        executor = executor if executor else "UNKNOW_EXECUTOR"

    findings.append(
        Finding({
            "name": "multisig event tracker",
            "description": "track executed transaction from multi-sig",
            "type": FindingType.Info,
            "severity": FindingSeverity.Info,
            "metadata": {
                'hash': msg_hash,
                'executor': executor
            }
        })
    )