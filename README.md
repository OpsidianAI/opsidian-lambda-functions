# Opsidian Lambda Functions

This is a collection of Lambda Functions for [Opsidian](http://opsidian.ai), a chatbot for Slack designed to make the life of ops teams easier.
With Opsidian you can invoke Lambda Functions in your AWS account directly from Slack.

For details, visit [Opsidian docs](http://opsidian.ai/lambda/).

## Prerequisites

* [Opsidian](http://opsidian.ai/install/)

## Using Opsidian Lambda Functions

In order to use an Opsidian Lambda Function you need to:

1. Create a Lambda Function in your AWS account.

2. Define which command should trigger the function, using the [Opsidian Dashboard](https://dashboard.opsidian.ai) ("Lambda functions" tab).

3. Run the command in Slack:

```
/ops run <command> [args]
```


## Contributing

We invite everyone to contribute to Opsidian Lambda Functions. Please check out the [Contributing Guide](CONTRIBUTING.md) for guidelines about how to proceed.

## License
Opsidian Lambda Functions are released under the [MIT LICENSE](LICENSE).