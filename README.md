# Databricks Custom Bundle Templates

This repository contains custom templates for Databricks Asset Bundles (DAB), organized into:

- `app/`: Templates for Databricks apps and no other resources
- `jobs/`: Templates for Databricks jobs and lakeflow declarative pipelines
- `advanced/`: Templates with complex deployment patterns

## Getting Started

Use these templates as a starting point for creating your own Databricks Asset Bundles.

### Using Templates via CLI

1. Install the Databricks CLI:
```bash
brew tap databricks/tap
brew install databricks
```

See databricks-cli [installation instructions](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/cli/install) for other platforms/methods.

2. Create a new bundle from template:
```bash
databricks bundle init --template-dir <template_path> <destination_path>
```

Example:
```bash
databricks bundle init https://github.com/nklc/DAB_TEMPLATES_NKLC --template-dir apps/default_app_w_warehouse .
```

3. Configure and deploy your bundle:
```bash
cd <bundle_name>
databricks bundle deploy -t dev
```

## Useful Links

- [Databricks Asset Bundles Overview](https://docs.databricks.com/aws/en/dev-tools/bundles/)
- [Databricks Asset Bundles Tutorials](https://docs.databricks.com/aws/en/dev-tools/bundles/tutorials)
- [Databricks Asset Bundles Configuration Reference](https://docs.databricks.com/aws/en/dev-tools/bundles/reference)
- [Databricks Asset Bundles Resource Reference](https://docs.databricks.com/aws/en/dev-tools/bundles/resources)
- [Databricks Custom Bundle Templates Documentation](https://docs.databricks.com/aws/en/dev-tools/bundles/templates#custom-templates)
- [Bundle Template Creation Tutorial](https://docs.databricks.com/aws/en/dev-tools/bundles/template-tutorial)

