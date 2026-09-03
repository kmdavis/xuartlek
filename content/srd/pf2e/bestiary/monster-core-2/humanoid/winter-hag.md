---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Winter Hag"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Winter Hag"
level: 7
source: "Monster Core 2"
aon_id: "creature-4434"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4434"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Winter Hag"
level: "Creature 7"
size: "Medium"
trait_01: "Hag"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, _see the unseen_, snow vision"
languages: "Aklo, Common, Fey, Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +13, Deception +17, Diplomacy +15, Occultism +15, Survival +14"
abilityMods: [4, 2, 3, 4, 3, 6]
abilities_top:
  - name: "Coven"
    desc: "A winter hag adds _howling blizzard_, _rewrite memory_, and _wall of ice_ to their coven's spells."
  - name: "Snow Vision"
    desc: "Snow doesn't impair a winter hag's vision; they ignore concealment from snowfall."
  - name: "Items"
    desc: "_+1 staff_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +13; __Will__: +16"
hp: 145
health:
  - name: "HP"
    desc: "145; __Immunities__ cold, emotion; __Weaknesses__ cold iron 5, fire 5, thaw the heart"
abilities_mid:
  - name: "Thaw the Heart"
    desc: "If the hag observes a creature succeed at a Performance check with a result equal to or greater than 26, the hag becomes slowed 1 and loses their immunity to emotion effects for 1 hour."
speed: "25 feet; ice climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _ice staff_ +17 (Magical, two-hand d8) __Damage__ 2d4+7 bludgeoning plus 1d6 cold"
  - name: "Melee"
    desc: "⬻ claw +16 (Agile) __Damage__ 2d6+7 slashing plus 1d6 cold"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, occult, polymorph) The winter hag can take on the appearance of any Medium humanoid woman. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Ice Climb"
    desc: "A winter hag can Climb at the listed Speed, but only on ice. They ignore difficult terrain from ice and snow, and they don't risk falling when crossing ice."
  - name: "Kiss of Rime"
    desc: "⬻ (Cold, Occult)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "A shard of magic ice embeds itself within the flesh of a creature within 30 feet. The creature must save against the curse of the frozen heart."
  - name: "Cruse of the Frozen Heart"
    desc: "(Curse)"
  - name: "Saving Throw"
    desc: "DC 25 Will"
  - name: "Stage 1"
    desc: "3d6 cold damage (1 day)"
  - name: "Stage 2"
    desc: "the target has resistance 5 to cold (1 day)"
  - name: "Stage 3"
    desc: "the target has resistance 10 to cold and treats no one as an ally (1 day)"
  - name: "Stage 4"
    desc: "the target is immune to cold, treats no one as an ally, and is unfriendly to all creatures it wasn't hostile to (1 day)"
  - name: "Stage 5"
    desc: "target becomes immune to cold and emotion effects, ceases to age, and is permanently _dominated_ by the hag—if the hag is dead, the target remains at stage 4"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ Frostbite - __3rd__ Enthrall, Environmental Endurance (at will), Paralyze - __4th__ Charm, Fly, Ice Storm, Rewrite Memory - __5th__ Howling Blizzard - __Constant (4th)__ See the Unseen"
sourcebook: "_Monster Core 2_, page 187."
```

```encounter-table
name: Winter Hag
creatures:
  - 1: Winter Hag
```
