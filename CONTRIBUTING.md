# Contributing to Opsidian Lambda Functions

First off, thank you for considering contributing to Opsidian Lambda Functions.
If you haven't already, join Opsidian's community on Slack ([request an invite](https://opsidian.ai/slack/)).

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [help@opsidian.ai](mailto:help@opsidian.ai).

## The structure of the repo

Each Lambda Function should be placed in a separate folder. The folder name should be lowercase, with words separated by a dash. The folder name should describe the function's purpose.

Each folder should contain a README.md file with the description of the purpose and usage of the Lambda Function.

### Documentation

We require all Lambda Functions to contain a documentation header in the following format:

```
# Description
#   <description of the function's functionality>
#
# Dependencies:
#   "<module name>": "<module version>"
#
# Environment variables:
#   LIST_OF_ENV_VARS_TO_SET
#
# Arguments:
#   <argument> - <description>
#
# Notes:
#   <additional information>
#
# Author:
#   <github username of the author>
```

## How to contribute

### Reporting bugs

If you've found a problem in Opsidian Lambda Functions please first check if the issue has already been reported. If you are unable to find any open GitHub issues addressing the problem you found, your next step will be to open a new one. Please use the [issue template](ISSUE_TEMPLATE.md) and include as many details as possible to help us resolve the issue faster.

### Submitting ideas and suggesting enhancements

To submit an idea or suggest an enhancement, please create an issue and provide a detailed description.

### Submitting changes

Please send a pull request to Opsidian Lamdba Functions with a clear list of what you've done. Always write a clear log message for your commits.

