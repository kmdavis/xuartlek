---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Empyreal Dragon"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Empyreal Dragon"
level: 14
source: "Monster Core"
aon_id: "creature-2942"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2942"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Empyreal Dragon"
level: "Creature 14"
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision, lifesense (imprecise) 30 feet, scent (imprecise) 60 feet"
languages: "Chthonian, Common, Diabolic, Draconic, Empyrean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +26, Athletics +28, Diplomacy +25, Heaven Lore +26, Intimidation +25, Medicine +28, Religion +28, Society +24"
abilityMods: [8, 4, 6, 4, 7, 5]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +24; __Ref__: +24; __Will__: +26 +2 status to all saves vs. divine"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ fear, paralyzed, sleep; __Weaknesses__ unholy 10"
abilities_mid:
  - name: "Inspiring Presence"
    desc: "(aura, emotion, mental) 20 feet. The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
  - name: "Divine Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit by an attack"
  - name: "Effect"
    desc: "Divine power intercedes, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
speed: "70 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +28 (Holy, reach 15 feet) __Damage__ 3d10+11 piercing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ claws +28 (Agile, Holy, reach 10 feet) __Damage__ 3d8+11 slashing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ tail +26 (Holy, reach 20 feet) __Damage__ 3d10+11 bludgeoning plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ wing +26 (Agile, Holy, reach 15 feet) __Damage__ 2d10+11 slashing plus 1d8 spirit"
abilities_bot:
  - name: "Direct Halo"
    desc: "⬻ (Concentrate, Divine, Manipulate) The dragon tosses their halo to a square within 90 feet. While the halo is deployed in this way, the dragon loses their inspiring presence aura, and the aura instead emanates from the halo with the same emanation radius. The dragon can Sustain to recall the halo from any distance. The halo is made of pure light—it doesn't occupy space and can't be targeted or destroyed in any way."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Spirit Breath whenever they score a critical hit with a Strike."
  - name: "Halo Pulse"
    desc: "⬺ (Concentrate, Divine) The dragon chooses one effect to impose on creatures in their inspiring presence aura. The dragon can't use Halo Pulse again for 1d4 rounds."
  - name: "Repulsion"
    desc: "Each creature must succeed at a DC 34 Fortitude save or be pushed until it's no longer in the aura."
  - name: "Restoration"
    desc: "(healing, vitality) Each creature recovers 7d8 Hit Points."
  - name: "Spirit Breath"
    desc: "⬺ (Divine, Holy, Spirit) The dragon unleashes a blast of holy fire that deals 12d8 spirit damage in a 50-foot cone (DC 34 basic Reflex save). The dragon can't use Spirit Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26 - __5th__ Holy Light (at will) - __7th__ Heal, Interplanar Teleport (at will; self only) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 115."
```

```encounter-table
name: Adult Empyreal Dragon
creatures:
  - 1: Adult Empyreal Dragon
```
