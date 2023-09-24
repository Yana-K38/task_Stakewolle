import requests
import base64


def get_akash_transactions(block_number):
    """
    Retrieve transactions from the Akash blockchain for a specified block number.
    Args:
        block_number (int): The block number for which to retrieve transactions.
    Returns:
        bytes: Binary transaction data retrieved from the Akash blockchain block.
    """
    rpc_server = "https://rpc.akashnet.net:443"
    response = requests.get(f"{rpc_server}/block?height={block_number}")
    if response.status_code == 200:
        block_data = response.json()
        txs_base64 = block_data.get("result", {}).get("block", {}).get("data", {}).get("txs", [])
        if txs_base64:
            txs_binary = [base64.b64decode(tx) for tx in txs_base64]
            for tx in txs_binary:
                return tx
        else:
            return "There are no transactions in the specified block."
    else:
        return f"Error when requesting data about the {block_number} block. Error code: {response.status_code}"


if __name__ == "__main__":
    block_number = 12949776
    print(get_akash_transactions(block_number))

