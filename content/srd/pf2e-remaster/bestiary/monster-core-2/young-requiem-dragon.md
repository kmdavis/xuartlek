---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Requiem Dragon"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Requiem Dragon"
level: 11
source: "Monster Core 2"
aon_id: "creature-4357"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4357"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Requiem Dragon"
level: "Creature 11"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision, lifesense 60 feet, scent (imprecise) 60 feet, status sight"
languages: "Chthonian, Common, Daemonic, Draconic, Empyrean, Requian"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Athletics +23, Diplomacy +21, Medicine +26, Religion +23, River of Souls Lore +21"
abilityMods: [7, 4, 5, 4, 7, 5]
abilities_top:
  - name: "Soul Journey"
    desc: "(divine, exploration) The dragon spends 1 hour traveling through planar channels to reach the River of Souls, and then reaches any point along the river. This has the effects of _interplanar teleport_, except that the dragon can arrive precisely where they like on any major plane."
  - name: "Status Sight"
    desc: "The requiem dragon automatically knows the Hit Points of all creatures they can see."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +18; __Will__: +24 +2 status to all saves vs. divine"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ death effects, paralyzed, sleep"
abilities_mid:
  - name: "Soul Anchor"
    desc: "⬲ (divine)"
  - name: "Trigger"
    desc: "A creature within 60 feet would drop to 0 Hit Points"
  - name: "Effect"
    desc: "The dragon anchors the triggering creature's soul to its body. The creature remains at 1 Hit Point, becomes doomed 2, and gains fast healing equal to the dragon's level for 1 minute. The creature becomes temporarily immune to further Soul Anchor usages for 24 hours."
  - name: "Withhold Death"
    desc: "⬲ (divine)"
  - name: "Trigger"
    desc: "The dragon is critically hit by an attack"
  - name: "Effect"
    desc: "The dragon resists the loosening of its own soul, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
speed: "40 feet, fly 120 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +24 (Magical, reach 10 feet) __Damage__ 2d10+10 piercing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ claw +24 (Agile, magical) __Damage__ 2d8+10 slashing plus 1d8 spirit and Grab"
  - name: "Melee"
    desc: "⬻ tail +22 (Magical, reach 15 feet) __Damage__ 2d8+10 bludgeoning plus 1d8 spirit"
abilities_bot:
  - name: "Dooming Breath"
    desc: "⬺ (Divine, spirit) Energy from Creation's Forge erupts from the dragon's mouth, dealing 9d8 spirit damage in a 60-foot line (DC 30 basic Reflex save). Undead creatures who fail the save must also succeed at a DC 30 Will save or become doomed 1. If the target is already doomed, the doomed value increases by 1 (to a maximum of doomed 4). The dragon can't use Dooming Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Dooming Breath whenever they score a critical hit with a Strike."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 27 - __Cantrips (5th)__ Stabilize - __4th__ Heal (×3) - __5th__ Heal (×2)"
sourcebook: "_Monster Core 2_, page 126."
```

```encounter-table
name: Young Requiem Dragon
creatures:
  - 1: Young Requiem Dragon
```
