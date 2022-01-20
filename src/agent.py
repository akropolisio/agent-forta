import forta_agent
from forta_agent import Finding, FindingType, FindingSeverity
from src.constants import MULTI_SIG_MAINNET_ADDRESS, ADDRESS_LIST

def handle_transaction(transaction_event: forta_agent.transaction_event.TransactionEvent):
    findings = []
    if transaction_event.to != MULTI_SIG_MAINNET_ADDRESS:
        return findings
    targeted_address = transaction_event.from_
    if targeted_address in ADDRESS_LIST:
        findings.append(
            Finding({
                'name': 'multisig tracker',
                'description': f'track interaction between {targeted_address} with multisig protocol',
                'type': FindingType.Info,
                'alert_id': "MultiSig_ALERT",
                'severity': FindingSeverity.Info,
                'metadata': {
                    "address": targeted_address
                }
            })
        )
    return findings