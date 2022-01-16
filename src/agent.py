from forta_agent import Finding, FindingType, FindingSeverity
from .constants import (
    MY_ADDRESS
)

def handle_transaction(transaction_event):
    findings = []
    # filter the transaction from the contract
    multisig_invocations = transaction_event.filter_function(
        # multi-sig_pausable_abi, and multi-sig-address
    )

    # filter transaction info from multi-sig
    for invocation in multisig_invocations:
        sender = transaction_event

        findings.append(
            Finding(
                {
                    "name": "MultiSig function listening",
                    "description": f"Function call by sender",
                    "type": Finding.suspicious,
                    "severity": get_severity(sender),
                    "metadata": {
                        "from": transaction_event.from_,
                        "to": transaction_event.to_
                    }
                }
            )
        )
    return findings


def get_severity(sender):
    if sender == MY_ADDRESS:
        return FindingSeverity.Medium
    else:
        return FindingSeverity.Critical