---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dweomercat"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Dweomercat"
level: 7
source: "Monster Core 2"
aon_id: "creature-4375"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4375"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Dweomercat"
level: "Creature 7"
size: "Medium"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, _detect magic_, scent (imprecise) 30 feet"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Arcana +16, Nature +15, Stealth +17, Survival +15"
abilityMods: [4, 4, 3, 3, 4, 5]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +12; __Ref__: +17; __Will__: +17 +1 status to all saves vs. magic"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Alter Dweomer"
    desc: "⬲ (arcane)"
  - name: "Trigger"
    desc: "The dweomercat is targeted by a spell or is within the area of a spell as it's cast"
  - name: "Effect"
    desc: "The dweomercat's runelike patterns start to glow as it gains an effect related to the tradition of the triggering spell. This effect occurs before the dweomercat is affected by the triggering spell. The effect lasts for 1 minute, until the dweomercat uses this ability again, or until the dweomercat Dismisses the effect, whichever comes first."
  - name: "Arcane"
    desc: "Magical feedback deals 4d6 force damage to the triggering spellcaster (DC 22 basic Reflex save)."
  - name: "Divine"
    desc: "The dweomercat gains a +1 status bonus to all skill checks."
  - name: "Occult"
    desc: "The dweomercat becomes invisible. This effect ends if the dweomercat uses a hostile action, in addition to the normal end conditions."
  - name: "Primal"
    desc: "The dweomercat gains 10 temporary Hit Points."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +17 (Magical) __Damage__ 2d10+7 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +17 (Agile, magical) __Damage__ 2d8+7 slashing"
abilities_bot:
  - name: "Dweomer Leap"
    desc: "⬺ (Arcane, teleportation)"
  - name: "Prerequisites"
    desc: "The dweomercat has at least one _translocate_ spell remaining"
  - name: "Effect"
    desc: "The dweomercat casts _translocate_, then can make a melee Strike against one creature adjacent to it at the end of its teleport. If the dweomercat ends its teleport adjacent to a creature under an ongoing spell effect or who cast a spell since the dweomercat's last turn, this does not expend a casting of _translocate_."
  - name: "Pounce"
    desc: "⬻ The dweomercat Strides and makes a Strike at the end of that movement. If the dweomercat began this action hidden, it remains hidden until after this ability's Strike. Dweomercat Familiars Particularly powerful spellcasters sometimes take young dweomercat cubs as familiars. Their independence and flightiness make dweomercats somewhat unreliable allies, though, so one is never sure whether their bond with a dweomercat will be long-lasting or a temporary affair."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 25 - __4th__ Dispel Magic (at will), Dispelling Globe, Translocate (×3) - __Constant (4th)__ Detect Magic"
sourcebook: "_Monster Core 2_, page 141."
```

```encounter-table
name: Dweomercat
creatures:
  - 1: Dweomercat
```
