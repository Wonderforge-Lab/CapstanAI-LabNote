# Simplified-Chinese Governance Batch Review Brief

Target locale: `zh-CN`
Review targets:

- `docs/branding.md`
- `PRIVACY.md`
- `SECURITY.md`
- `CONTRIBUTING.md`

Status: language, cultural and semantic-parity review before publishing the remaining Chinese front-door governance documentation.

## Review goal

Please review these four files as one small governance/identity batch.

The Chinese should be natural to a mainland Simplified-Chinese technical reader while preserving the exact meaning and force of the English source.

This batch has two different registers:

1. `branding.md` may retain some imagery and cadence.
2. `PRIVACY.md`, `SECURITY.md`, and `CONTRIBUTING.md` should remain concise, technical and unambiguous.

Do not make governance statements stronger or weaker merely for stylistic smoothness.

## Terminology baseline

Follow the reviewed `GLOSSARY.md` where relevant.

Product marks remain unchanged:

```text
CapstanAI
LabNote
WonderForge
```

Keep GitHub/Git terms such as `pull request`, `issue`, `fork`, `runner`, and product UI names in English where that makes the actual GitHub control easier to identify.

## File-specific stress tests

### 1. Branding

Please check:

- whether `生态体系与总品牌` naturally conveys ecosystem + umbrella,
- whether the capstan mechanical explanation is understandable,
- whether `受治理的多头 AI 工作流系统` is technically natural,
- whether `手动、基于文件的实验笔记本` correctly conveys manual file-based lab notebook,
- whether the closing three lines preserve the original concise branding cadence:

```text
WonderForge 在幕布上。
CapstanAI 在招牌上。
LabNote 在盒子上。
```

If you can improve the cadence without changing the brand hierarchy, please propose it.

### 2. Privacy

Please verify that the Chinese clearly says this repository is intended only for small text artifacts safe for public exposure.

Stress-test these distinctions:

- private data,
- private chat transcripts,
- credentials,
- personal records,
- private project material,
- external private storage,
- exposing names/account details/local paths.

Please flag any term that sounds legalistic or narrower/broader than the English.

### 3. Security

This file must preserve strong safety language.

Please verify that the Chinese unambiguously says:

- use GitHub private vulnerability reporting for security vulnerabilities,
- do not put sensitive security details in public issues,
- if private vulnerability reporting is unavailable, a public issue may only request a private contact route and must not include secrets/sensitive details,
- examples/packets must not contain credentials, tokens, keys, or private connection details,
- LabNote does not run code, start services, or execute packet instructions,
- files are human-reviewed artifacts,
- if sensitive material appears in a public packet, remove it and rotate any exposed secret outside this project.

Please pay particular attention to whether `秘密信息` is the best Chinese term for `secret` in this security context, and whether `轮换任何已经暴露的秘密信息` naturally conveys credential/secret rotation.

### 4. Contributing

Please verify that the Chinese preserves these distinctions:

- the canonical repository is collaborator-maintained,
- **outside pull requests are not accepted**,
- people may still inspect, fork and adapt the public scaffold under Apache-2.0,
- public-safe bug/documentation reports may be opened as issues,
- security reports belong in private vulnerability reporting,
- collaborator changes must preserve human-in-the-loop design,
- agents/runners/background services/automation must not be added unless the project explicitly changes direction,
- examples should be fictional,
- private identifiers and internal project references should be avoided,
- small text artifacts belong here; bulky material belongs elsewhere.

The phrase `不接受外部 pull request` should read as a firm repository policy, not a suggestion.

## Cross-file consistency

Please compare all four files for consistent use of:

- public / public-safe,
- private,
- sensitive,
- credentials,
- token,
- secret / key,
- human review,
- canonical,
- repository,
- project material.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. technical register,
3. cultural fit,
4. semantic parity,
5. safety/policy language strength,
6. cross-file terminology consistency,
7. whether the batch is ready after listed edits.

### Part B - recommended edits

For each change:

```text
File:
Section:
Current Chinese:
Recommended Chinese:
Reason:
Semantic effect: unchanged / clearer / potential meaning change
Confidence: high / medium / low
```

Do not rewrite natural passages merely for preference.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If another pass is required, identify the blocking language, safety or policy issue clearly.
