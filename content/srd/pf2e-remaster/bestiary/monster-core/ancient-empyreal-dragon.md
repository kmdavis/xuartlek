---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Empyreal Dragon"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Empyreal Dragon"
level: 19
source: "Monster Core"
aon_id: "creature-2943"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2943"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ancient Empyreal Dragon"
level: "Creature 19"
size: "Gargantuan"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
trait_04: "Uncommon"
modifier: 35
perception:
  - name: "Perception"
    desc: "Perception +35; darkvision, lifesense (imprecise) 30 feet, scent (imprecise) 60 feet"
languages: "Chthonian, Common, Diabolic, Draconic, Empyrean, Fey, Necril; truespeech"
skills:
  - name: "Skills"
    desc: "Acrobatics +31, Athletics +35, Diplomacy +31, Intimidation +31, Heaven Lore +32, Medicine +35, Religion +32, Society +30"
abilityMods: [10, 6, 8, 5, 8, 6]
ac: 43
armorclass:
  - name: "AC"
    desc: "43; __Fort__: +31; __Ref__: +31; __Will__: +35 +2 status to all saves vs. divine"
hp: 350
health:
  - name: "HP"
    desc: "350; __Immunities__ fear, paralyzed, sleep; __Weaknesses__ unholy 15"
abilities_mid:
  - name: "Inspiring Presence"
    desc: "(aura, emotion, mental) 20 feet. The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
  - name: "Divine Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit by an attack"
  - name: "Effect"
    desc: "Divine power intercedes, preventing some of the damage. The dragon gains resistance 15 to all damage against the triggering attack."
speed: "80 feet, fly 200 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +35 (Holy, Magical, reach 20 feet) __Damage__ 4d10+16 piercing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ claws +35 (Agile, Holy, Magical, reach 15 feet) __Damage__ 4d8+16 slashing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ tail +33 (Holy, Magical, reach 25 feet) __Damage__ 4d10+16 bludgeoning plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ wing +33 (Agile, Magical, reach 20 feet) __Damage__ 3d10+16 slashing plus 1d8 spirit"
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
    desc: "Each creature must succeed at a DC 41 Fortitude save or be pushed until it's no longer in the aura."
  - name: "Restoration"
    desc: "(healing, vitality) Each creature recovers 9d8 Hit Points."
  - name: "Restriction"
    desc: "(incapacitation, mental) Creatures must succeed at a DC 41 Will save or be slowed 1 (slowed 2 on a critical failure) while they remain within the aura. Regardless of the result, a creature is then temporarily immune to restriction for 1 minute."
  - name: "Spirit Breath"
    desc: "⬺ (Divine, Holy, Spirit) The dragon unleashes a blast of holy fire that deals 16d8 spirit damage in a 50-foot cone (DC 41 basic Reflex save). The dragon can't use Spirit Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 41, attack +33 - __7th__ Holy Light (at will), Interplanar Teleport (at will; self only) - __9th__ Heal - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 116."
```

```encounter-table
name: Ancient Empyreal Dragon
creatures:
  - 1: Ancient Empyreal Dragon
```
