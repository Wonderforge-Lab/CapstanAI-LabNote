# Simplified-Chinese First-Release Completeness Review Brief

Target locale: `zh-CN`

This is a narrow final translation-surface review before adversarial parity testing.

## Review targets

- `lobby/README.md`
- `registry/README.md`
- `registry/TAG_DISPLAY_CATALOG.md`

## Context

The end-to-end routine-deposit specimen has passed protocol, machine-schema, path, signoff and behavioural-compatibility review. Its only proposed terminology edit (`依据材料` -> `佐证材料`) was not adopted because the frozen glossary explicitly rejects global replacement with `佐证材料`.

All previously reviewed operational documents and templates remain unchanged except for final routing cleanup:

- temporary fallback-to-English clauses were removed from the Chinese `AI_ENTRYPOINT.md` now that the referenced Chinese policy files exist;
- the Chinese `ROUTINE_DEPOSIT_QUICKSTART.md` now points directly to reviewed Chinese policy/template companions while keeping JSON schema and runtime paths canonical.

The three files in this review are the remaining inventory/support surfaces identified by the completeness sweep.

## 1. Lobby README

Please verify:

- `入口区` remains the frozen rendering of `lobby`;
- the reading order is correct;
- public/reference-only workspace safety remains strong;
- the localized file does **not** accidentally imply a localized runtime registry;
- this sentence is clear:

```text
在仓库根目录的基准 registry/ 路径下创建 JSON 登记记录。
```

The explicit `仓库根目录` wording is intentional because the localized README itself lives under `locales/zh-CN/lobby/`; a literal relative translation of the English `../registry/` would point to the wrong localized directory.

Please also review:

```text
入口区留下的是工作轨迹，不是登录系统。
```

The intended source meaning is: the lobby creates a paper trail, not an authentication/login mechanism.

## 2. Registry README

Please verify:

- the file is clearly a localized explanation only;
- canonical live runtime path remains root `registry/`;
- canonical records remain JSON-per-record;
- CSV remains legacy/optional rollup;
- visitors do not edit CSV unless the operator explicitly asks.

Stress-test:

```text
本文件是仓库根目录 registry/README.md 的简体中文说明，不改变基准运行期路径 registry/。
```

It must not suggest that `locales/zh-CN/registry/` is a runtime registry.

## 3. Tag display catalog

The catalog is a presentation layer only.

Canonical tag records remain:

```text
registry/tags/accepted/*.json
```

Canonical slugs must remain unchanged.

Please verify the Chinese display names/descriptions are natural and faithful:

```text
capstanai-labnote -> CapstanAI - LabNote
example-project -> 示例项目
human-in-the-loop -> 人在回路（HITL）
provenance -> 溯源信息
workflow-testing -> 工作流测试
```

The catalog must not imply:

- a second localized tag registry,
- translated machine slugs,
- changed tag status/scope/authority,
- that the Chinese display catalog is more authoritative than the canonical JSON records.

## Final readiness question

If these three files pass, please state whether the **first-release human/AI-facing translation surface is complete enough to move from translation review into adversarial parity testing**.

This does not mean the locale should yet be marked fully `supported`. The next gate is behavioural/adversarial parity.

## Review format

### Part A

Cover:

1. naturalness,
2. developer/agent-facing register,
3. lobby path/routing clarity,
4. registry-path invariance,
5. JSON-vs-CSV parity,
6. tag-display/canonical-slug separation,
7. first-release surface completeness,
8. readiness for adversarial parity testing.

### Part B

For each recommended edit:

```text
File:
Section / wording:
Current Chinese:
Recommended Chinese:
Reason:
Protocol effect: unchanged / clearer / potential behaviour change
Confidence: high / medium / low
```

End with:

```text
READY FOR ADVERSARIAL PARITY AFTER LISTED EDITS
READY FOR ADVERSARIAL PARITY AS WRITTEN
REQUIRES ANOTHER TRANSLATION REVIEW PASS
```
