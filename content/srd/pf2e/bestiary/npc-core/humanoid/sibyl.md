---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sibyl"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Sibyl"
level: 3
source: "NPC Core"
aon_id: "creature-3443"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3443"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Sibyl"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +9, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +9, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +11"
abilityMods: [0, 3, -1, 2, 2, 4]
abilities_top:
  - name: "Induce Awe"
    desc: "The sibyl can use [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] instead of [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Coerce|Coerce]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]]."
  - name: "Items"
    desc: "bundles of herbs, Dagger"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +8; __Will__: +12"
hp: 40
health:
  - name: "HP"
    desc: "40"
abilities_mid:
  - name: "Foresight"
    desc: "⬲"
  - name: "Trigger"
    desc: "The sibyl becomes the target of a spell with the [[srd/pf2e/compendium/rules-elements/traits/player-core/detection|detection]], [[srd/pf2e/compendium/rules-elements/traits/player-core/prediction|prediction]], [[srd/pf2e/compendium/rules-elements/traits/player-core/revelation|revelation]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/scrying|scrying]] trait"
  - name: "Effect"
    desc: "The sibyl's oracular awareness alerts them to danger. They gain a +2 circumstance bonus to their saving throw or AC against the spell."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing plus 1d6 spirit"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning plus 1d6 spirit"
  - name: "Ranged"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing plus 1d6 spirit"
abilities_bot:
  - name: "Divine Frenzy"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Requirements"
    desc: "The sibyl isn't [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] or in a frenzy"
  - name: "Effect"
    desc: "The sibyl enters into a divine frenzy that lasts 1 minute. The sibyl can't voluntarily stop frenzying. While in a divine frenzy, the sibyl takes a –2 penalty to Perception checks and Will saves and gains a +2 status bonus to their spell DC and spell attack modifier. During a divine frenzy, the sibyl can't use actions with the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait unless they're Casting a Spell or [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seeking]]. The frenzy lasts for 1 minute, until the sibyl falls [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], or the encounter ends, whichever comes first. The sibyl can't voluntarily end the frenzy."
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 19, attack +11 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/haunting-hymn|Haunting Hymn]], [[srd/pf2e/compendium/spells/cantrips/know-the-way|Know the Way]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/command|Command]], [[srd/pf2e/compendium/spells/rank-1/concordant-choir|Concordant Choir]], [[srd/pf2e/compendium/spells/rank-1/fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/mindlink|Mindlink]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/augury|Augury]], [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]], [[srd/pf2e/compendium/spells/rank-2/sudden-blight|Sudden Blight]] (3 slots) __Oracle Focus Spells 1 Focus Point,__ DC 19 - __2nd__ [[srd/pf2e/compendium/spells/focus/brain-drain|Brain Drain]]"
sourcebook: "_NPC Core_, page 30."
```

```encounter-table
name: Sibyl
creatures:
  - 1: Sibyl
```
