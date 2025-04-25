# Swagger Codegen Upgrade Guide

This guide outlines the necessary steps to upgrade our customized version of the Swagger Codegen (OpenAPI Generator) library and deploy it to Artifactory.

---

## 🚀 Steps to Upgrade

### 1. Sync the Forked Repository

We maintain a fork of the OpenAPI Generator:

🔗 [EENCloud/openapi-generator](https://github.com/EENCloud/openapi-generator)

- Ensure your local fork is in sync with the upstream `main` branch.
- Go to the GitHub page of the fork, click **Sync fork**, then click **Update branch**.
- If nothing happens or you're unable to perform the update, contact **Wouter** for help (you might lack the required permissions).

---

### 2. Apply Custom Changes

We maintain two custom patches that need to be applied to the latest `main` branch. It's recommended to do this in a **new release branch**:

- [`Feature/enum as string cm (#2)`](https://github.com/OpenAPITools/openapi-generator/commit/fbfd515)
- [`Fix import mapping for code generation (#1)`](https://github.com/OpenAPITools/openapi-generator/commit/2461ea7)

Apply both patches on top of the updated main branch before proceeding to build.

---

### 3. Build and Deploy to Artifactory

Use the following Maven command to build the required modules:

```bash
mvn clean install -pl modules/openapi-generator-gradle-plugin -am -DskipTests -ntp -U
```

Deploy the generated artifacts to the following Artifactory locations:

- [openapi-generator](https://artifactory-oss.aus1bld1.cameramanager.com/ui/repos/tree/General/libs-release-local/org/openapitools/openapi-generator)
- [openapi-generator-core](https://artifactory-oss.aus1bld1.cameramanager.com/ui/repos/tree/General/libs-release-local/org/openapitools/openapi-generator-core)
- [openapi-generator-project](https://artifactory-oss.aus1bld1.cameramanager.com/ui/repos/tree/General/libs-release-local/org/openapitools/openapi-generator-project)
- [openapi-generator-gradle-plugin](https://artifactory-oss.aus1bld1.cameramanager.com/ui/repos/tree/General/plugins-release-local/org/openapitools/openapi-generator-gradle-plugin)

---

### 4. Update Mustache Files

We use customized mustache templates for Java Spring code generation. These need to be copied and applied to the new version:

- Source templates:  
  [`modules/openapi-generator/src/main/resources/JavaSpring`](https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/JavaSpring)

Then:

- Update the `gradle.properties` file to set the new `openapiPluginVersion`.
- Modify the `api-generator.gradle` file to point to the updated mustache file directory.

Refer to this PR as an example:  
🔗 [PR #5076 — java-services](https://github.com/EENCloud/java-services/pull/5076)

---

## ✅ Final Checklist

- [ ] Fork is synced with upstream `main`
- [ ] Custom changes are applied in a new branch
- [ ] Artifacts are built and deployed
- [ ] Mustache files are updated
- [ ] `gradle.properties` and `api-generator.gradle` are updated accordingly
