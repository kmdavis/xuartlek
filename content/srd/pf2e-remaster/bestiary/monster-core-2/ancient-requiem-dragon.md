---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Requiem Dragon"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Requiem Dragon"
level: 20
source: "Monster Core 2"
aon_id: "creature-4359"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4359"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ancient Requiem Dragon"
level: "Creature 20"
size: "Gargantuan"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Uncommon"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; darkvision, lifesense 120 feet, scent (imprecise) 60 feet, status sight"
languages: "Chthonian, Common, Daemonic, Draconic, Empyrean, Requian"
skills:
  - name: "Skills"
    desc: "Acrobatics +32, Athletics +38, Diplomacy +34, Medicine +41, Religion +38, River of Souls Lore +34"
abilityMods: [10, 6, 7, 6, 10, 7]
abilities_top:
  - name: "Soul Journey"
    desc: "(divine, exploration) The dragon spends 1 hour traveling through planar channels to reach the River of Souls, and then reaches any point along the river. This has the effects of _interplanar teleport_, except that the dragon can arrive precisely where they like on any major plane."
  - name: "Status Sight"
    desc: "The requiem dragon automatically knows the Hit Points of all creatures they can see."
ac: 44
armorclass:
  - name: "AC"
    desc: "44; __Fort__: +33; __Ref__: +30; __Will__: +36"
hp: 370
health:
  - name: "HP"
    desc: "370; __Immunities__ death effects, paralyzed, sleep"
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
    desc: "The dragon resists the loosening of its own soul, preventing some of the damage. The dragon gains resistance 20 to all damage against the triggering attack."
speed: "60 feet, fly 180 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +38 (Magical, reach 20 feet) __Damage__ 4d10+15 piercing plus 2d8 spirit"
  - name: "Melee"
    desc: "⬻ claw +38 (Agile, magical, reach 15 feet) __Damage__ 4d6+15 slashing plus 2d8 spirit and Grab"
  - name: "Melee"
    desc: "⬻ tail +36 (Magical, reach 25 feet) __Damage__ 4d8+15 bludgeoning plus 2d8 spirit"
abilities_bot:
  - name: "Dooming Breath"
    desc: "⬺ (Divine, spirit) Energy from Creation's Forge erupts from the dragon's mouth, dealing 16d8 spirit damage in a 120-foot line (DC 42 basic Reflex save). Undead creatures who fail the save must also succeed at a DC 42 Will save or become doomed 1. If the target is already doomed, the doomed value increases by 1 (to a maximum of doomed 4). The dragon can't use Dooming Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Dooming Breath whenever they score a critical hit with a Strike."
  - name: "Redirect River"
    desc: "⬻ (Concentrate, death, divine) The requiem dragon redirects a small portion of the River of Souls, using their body as a spiritual connection. The river swells around them, filling the area in a 15-foot emanation for 1 round, becoming difficult terrain to all other creatures. Additionally, creatures that begin their turn in the emanation or enter it for the first time each round must succeed a DC 42 basic Fortitude save or become drained 1 and doomed 1. If the target is already drained or doomed, the value increases by 1 (to a maximum of 4). The dragon can Sustain the effect."
  - name: "Soul Shield"
    desc: "⬺ (Concentrate, divine)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The requiem dragon uses their life essence to create a shield of spiritual energy around a creature within 60 feet. The shield creates a link between the dragon and the creature with the effects of share life except that the effect doesn't end regardless of distance and remains for 1 hour. In addition, the creature gains resistance 10 to physical and spirit damage that applies to the half of damage it receives. The dragon can Dismiss the effect."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 39 - __Cantrips (10th)__ Stabilize - __9th__ Heal (×3) - __10th__ Heal (×2)"
sourcebook: "_Monster Core 2_, page 128."
```

```encounter-table
name: Ancient Requiem Dragon
creatures:
  - 1: Ancient Requiem Dragon
```
