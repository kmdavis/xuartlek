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
    desc: "Perception +30; darkvision, _truesight_"
languages: "Chthonian, Diabolic, Empyrean, Requian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +27, Deception +33, Intimidation +33, Occultism +27, Religion +30, Stealth +28"
abilityMods: [9, 3, 9, 2, 5, 8]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the _binding circle_ ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +32; __Ref__: +26; __Will__: +28"
hp: 380
health:
  - name: "HP"
    desc: "380; __Immunities__ fear; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Despoiler"
    desc: "(aura, divine) 1,000 feet. Creatures within the aura take a –2 circumstance penalty to all saving throws against poisons, diseases, and drugs."
speed: "40 feet, climb 20 feet; fly"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +34 (Magical, reach 10 feet, unholy) __Damage__ 3d12+17 piercing plus 2d6 spirit and sensory fever"
  - name: "Melee"
    desc: "⬻ claw +34 (Agile, magical, reach 15 feet, unholy) __Damage__ 3d8+17 slashing plus 2d6 spirit and sensory fever"
abilities_bot:
  - name: "Isolate Foes"
    desc: "⬺ (Curse, divine, emotion, incapacitation, mental)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The ximtal attempts to isolate its enemy's companions, forcing an impression that each creature's friends and allies have vanished, and they're all alone against an insurmountable threat. The ximtal chooses up to four creatures, each of whom must be adjacent to one other target. Each target must attempt a DC 38 Will save. On a failure, a target becomes out of phase with all allies. The affected creatures can't perceive their allies or interact with them in any way, and they can move into allies' spaces as if their allies simply weren't there. Allies similarly can't perceive or interact with the affected creatures with one exception: an ally can target an affected creature with an effect that specifically targets curses such as a 4th-rank _cleanse affliction_. Every 24 hours, an affected creature can attempt a new saving throw to end this effect."
  - name: "Sensory Fever"
    desc: "(disease) A ximtal's withering attacks cause a debilitating disease that targets the senses; Saving Throw DC 36 Fortitude"
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
    desc: "⬻ (Divine, teleportation) The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __Cantrips (9th)__ Detect Magic - __8th__ Desiccate (×3), Fear (at will), Quandary (×3), Suggestion (at will) - __Constant (9th)__ Fly, Truesight"
sourcebook: "_Monster Core 2_, page 277."
```

```encounter-table
name: Ximtal
creatures:
  - 1: Ximtal
```
