---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ximtal"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Ximtal"
level: 17
source: "Monster Core 2"
aon_id: "creature-4537"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4537"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ximtal"
level: "Creature 17"
size: "Large"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Requian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +33, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +33, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +27, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +30, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +28"
abilityMods: [9, 3, 9, 2, 5, 8]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the [[srd/pf2e/compendium/spells/rituals/binding-circle|_binding circle_]] ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +32; __Ref__: +26; __Will__: +28"
hp: 380
health:
  - name: "HP"
    desc: "380; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
abilities_mid:
  - name: "Despoiler"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 1,000 feet. Creatures within the aura take a –2 circumstance penalty to all saving throws against [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poisons]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|diseases]], and drugs."
speed: "40 feet, climb 20 feet; fly"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d12+17 piercing plus 2d6 spirit and sensory fever"
  - name: "Melee"
    desc: "⬻ claw +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d8+17 slashing plus 2d6 spirit and sensory fever"
abilities_bot:
  - name: "Isolate Foes"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The ximtal attempts to isolate its enemy's companions, forcing an impression that each creature's friends and allies have vanished, and they're all alone against an insurmountable threat. The ximtal chooses up to four creatures, each of whom must be adjacent to one other target. Each target must attempt a DC 38 Will save. On a failure, a target becomes out of phase with all allies. The affected creatures can't perceive their allies or interact with them in any way, and they can move into allies' spaces as if their allies simply weren't there. Allies similarly can't perceive or interact with the affected creatures with one exception: an ally can target an affected creature with an effect that specifically targets curses such as a 4th-rank [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|_cleanse affliction_]]. Every 24 hours, an affected creature can attempt a new saving throw to end this effect."
  - name: "Sensory Fever"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]) A ximtal's withering attacks cause a debilitating disease that targets the senses; Saving Throw DC 36 Fortitude"
  - name: "Stage 1"
    desc: "creature loses one sense determined randomly: hearing, sight, smell, or taste (1 day)"
  - name: "Stage 2"
    desc: "creature loses an additional sense from the stage 1 list (1 day)"
  - name: "Stage 3"
    desc: "creature loses an additional sense from the stage 1 list (1 day)"
  - name: "Stage 4"
    desc: "creature loses the last sense from the stage 1 list and any special senses, such as tremorsense or lifesense (1 day)"
  - name: "Stage 5"
    desc: "all lost senses are permanent unless restored via sound body or a similar effect"
  - name: "Skip Between"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]]) The sahkil moves from [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] to the [[srd/pf2e/compendium/gm/planes#Ethereal Plane|Ethereal Plane]] or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/desiccate|Desiccate]] (×3), [[srd/pf2e/compendium/spells/rank-1/fear|Fear]] (at will), [[srd/pf2e/compendium/spells/rank-8/quandary|Quandary]] (×3), [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]] (at will) - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-4/fly|Fly]], [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 277."
```

```encounter-table
name: Ximtal
creatures:
  - 1: Ximtal
```
