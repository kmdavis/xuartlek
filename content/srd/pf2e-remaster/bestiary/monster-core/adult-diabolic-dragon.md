---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Diabolic Dragon"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Diabolic Dragon"
level: 15
source: "Monster Core"
aon_id: "creature-2939"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2939"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Diabolic Dragon"
level: "Creature 15"
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; greater darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "Common, Diabolic, Draconic, Empyrean, Necril, Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +27, Athletics +30, Deception +26, Diplomacy +28, Hell Lore +24, Intimidation +26, Legal Lore +26, Religion +26, Society +24, Thievery +27"
abilityMods: [8, 4, 6, 3, 5, 5]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair the dragon's vision; they ignore the concealed condition from smoke."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +29; __Ref__: +25; __Will__: +26 +2 status to all saves vs. divine"
hp: 285
health:
  - name: "HP"
    desc: "285; __Immunities__ fire, paralyzed, sleep; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 90 feet, DC 34"
  - name: "Hell's Sting"
    desc: "⬲ (divine, mental, unholy)"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon channels the rancor of Hell back through the body of their foe, overwhelming it with an infernal assault on the mind. The triggering creature takes 8d6 mental damage with a DC 36 basic Will save. Holy creatures use an outcome one degree of success worse than they roll on their saving throw."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "60 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +30 (Fire, reach 15 feet, Magical, Unholy) __Damage__ 3d12+11 piercing plus 2d6 fire"
  - name: "Melee"
    desc: "⬻ claws +30 (Agile, Fire, Magical, Unholy, reach 10 feet) __Damage__ 3d8+11 piercing plus 2d6 fire and Grab"
  - name: "Melee"
    desc: "⬻ tail +28 (Fire, reach 20 feet, Magical, Unholy) __Damage__ 3d8+11 bludgeoning plus 2d6 fire and Improved Knockdown"
abilities_bot:
  - name: "Diabolic Fire"
    desc: "Any fire damage that a diabolic dragon deals, including fire damage from spells, is imbued with the unholy power of Hell to scorch the spirit as well. A creature takes spirit damage instead of fire damage if that would be more detrimental to the creature (as determined by the GM). A diabolic dragon is immune to the diabolic fire of other diabolic dragons, the fire from _divine immolation_, and similar effects."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hellfire Breath whenever they score a critical hit with a Strike."
  - name: "Hellfire Breath"
    desc: "⬺ (Divine, Fire, Unholy) The dragon unleashes a blast of infernal fire that deals 16d6 fire damage in a 50-foot cone (DC 36 basic Reflex save). The dragon can't use Hellfire Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26 - __Cantrips (8th)__ Ignition - __7th__ Divine Immolation, Interplanar Teleport (at will; self only), Wall of Fire (at will)"
sourcebook: "_Monster Core_, page 113."
```

```encounter-table
name: Adult Diabolic Dragon
creatures:
  - 1: Adult Diabolic Dragon
```
