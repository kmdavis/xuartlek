---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Diabolic Dragon"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Diabolic Dragon"
level: 20
source: "Monster Core"
aon_id: "creature-2940"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2940"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ancient Diabolic Dragon"
level: "Creature 20"
size: "Gargantuan"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 33
perception:
  - name: "Perception"
    desc: "Perception +33; greater darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "Aklo, Chthonian, Common, Diabolic, Draconic, Empyrean, Necril, Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +33, Athletics +38, Deception +34, Diplomacy +36, Hell Lore +33, Intimidation +34, Legal Lore +35, Religion +35, Society +33, Thievery +33"
abilityMods: [10, 5, 8, 5, 7, 8]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair the dragon's vision; they ignore the concealed condition from smoke."
ac: 44
armorclass:
  - name: "AC"
    desc: "44; __Fort__: +36; __Ref__: +32; __Will__: +32 +2 status to all saves vs. divine"
hp: 390
health:
  - name: "HP"
    desc: "390; __Immunities__ fire, paralyzed, sleep; __Weaknesses__ holy 15"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental 90 feet, DC 40)"
  - name: "Hell's Sting"
    desc: "⬲ (divine, mental, unholy)"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon channels the rancor of Hell back through the body of their foe, overwhelming it with an infernal assault on the mind. The triggering creature takes 10d6 mental damage with a DC 42 basic Will save. Holy creatures use an outcome one degree of success worse than they roll on their saving throw."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "70 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (Fire, Magical, reach 20 feet, Unholy) __Damage__ 4d12+18 piercing plus 2d6 fire"
  - name: "Melee"
    desc: "⬻ claws +38 (Agile, Fire, Magical, Unholy, reach 15 feet) __Damage__ 4d8+18 piercing plus 2d6 fire and Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +36 (Fire, Magical, reach 25 feet, Unholy) __Damage__ 4d8+18 bludgeoning plus 2d6 fire and Improved Knockdown"
abilities_bot:
  - name: "Diabolic Fire"
    desc: "Any fire damage that a diabolic dragon deals, including fire damage from spells, is imbued with the unholy power of Hell to scorch the spirit as well. A creature takes spirit damage instead of fire damage if that would be more detrimental to the creature (as determined by the GM). A diabolic dragon is immune to the diabolic fire of other diabolic dragons, the fire from _divine immolation_, and similar effects."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hellfire Breath whenever they score a critical hit with a Strike."
  - name: "Hellfire Breath"
    desc: "⬺ (Divine, Fire, Unholy) The dragon unleashes a blast of infernal fire that deals 21d6 fire damage in a 50-foot cone (DC 42 basic Reflex save). The dragon can't use Hellfire Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40, attack +32 - __Cantrips (10th)__ Ignition - __7th__ Interplanar Teleport (at will; self only) - __8th__ Summon Fiend (phistophilus only; at will) - __9th__ Divine Immolation (at will), Falling Stars (fire only), Wall of Fire (at will)"
sourcebook: "_Monster Core_, page 114."
```

```encounter-table
name: Ancient Diabolic Dragon
creatures:
  - 1: Ancient Diabolic Dragon
```
