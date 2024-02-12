import torch
import torch.nn.functional as F


def scaled_dot_product_attention(query, key, value, mask=None):
    # Calculate attention scores
    scores = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.tensor(query.shape[-1]).float())

    # Apply mask if provided
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-1e9'))  # Replace masked values with very negative numbers

    # Apply softmax to get attention weights
    attention_weights = F.softmax(scores, dim=-1)

    # Calculate weighted sum of values q
    output = torch.matmul(attention_weights, value)

    return output, attention_weights


# Example usage
query = torch.tensor([[0.1, 0.2, 0.3]])
key = torch.tensor([[0.4, 0.5, 0.6]])
value = torch.tensor([[1.0, 2.0, 3.0]])

output, attention_weights = scaled_dot_product_attention(query, key, value)
print("Output:", output)
print("Attention Weights:", attention_weights)
