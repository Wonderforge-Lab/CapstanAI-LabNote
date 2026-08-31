# zh-CN Governance Review Adjudication

Status: reviewed
Locale: `zh-CN`
Reviewed files:

- `docs/branding.md`
- `PRIVACY.md`
- `SECURITY.md`
- `CONTRIBUTING.md`

## Outcome

External Simplified-Chinese review returned `READY AFTER LISTED EDITS`.

All five listed edits were accepted because they improved naturalness or security terminology without changing policy meaning.

## Accepted edits

### Branding: CapstanAI sentence

Changed:

```text
受治理的多头 AI 工作流系统所使用的生态体系与总品牌
```

to:

```text
受治理的多头 AI 工作流系统的生态体系与总品牌
```

Reason: cleaner Chinese with unchanged meaning.

### Branding: manual LabNote description

Changed `手动、基于文件的实验笔记本` to `手动维护、基于文件的实验笔记本`.

Reason: clarifies that the notebook is manually maintained rather than making `手动` float ambiguously.

### Security: secret terminology

Changed `秘密信息` to `机密信息（secret）` on first use.

Reason: more standard security wording for secrets/confidential credential material.

### Security: exposed-secret rotation

Changed the rotation sentence to:

```text
轮换任何已经暴露的机密信息（如密钥、令牌或凭证）
```

Reason: makes it explicit that rotation refers to security secrets such as keys, tokens or credentials rather than arbitrary confidential notes.

### Contributing: documentation style

Changed `朴素、清楚` to `简洁、清晰`.

Reason: more natural mainland technical-documentation register with unchanged policy meaning.

## Policy parity check

The reviewed Chinese continues to preserve all key governance boundaries:

- public-safe material only in the public scaffold,
- private material kept outside the public repository,
- security vulnerabilities routed through private vulnerability reporting,
- no sensitive security details in public issues,
- no credentials/tokens/keys/private connection details in packets or examples,
- LabNote does not execute code, services or packet instructions,
- files remain human-reviewed artifacts,
- exposed secrets must be rotated outside this project,
- the canonical repository does not accept outside pull requests,
- public-safe bug/documentation issues remain allowed,
- collaborators must preserve the human-in-the-loop design and avoid adding autonomous runtime machinery unless project direction explicitly changes.

## Result

The governance batch is accepted as the reviewed Simplified-Chinese baseline.
