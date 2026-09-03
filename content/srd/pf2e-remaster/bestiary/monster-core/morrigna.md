---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Morrigna"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Morrigna"
level: 15
source: "Monster Core"
aon_id: "creature-3149"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3149"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Morrigna"
level: "Creature 15"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; darkvision, lifesense 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Necril, Requian; _speak with animals_, _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +27, Boneyard Lore +28, Diplomacy +27, Intimidation +29, Religion +29, Society +24, Stealth +27"
abilityMods: [8, 4, 4, 3, 6, 4]
abilities_top:
  - name: "Items"
    desc: "_+2 striking bo staff_"
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +25; __Ref__: +27; __Will__: +29 +1 status to all saves vs. magic"
hp: 240
health:
  - name: "HP"
    desc: "240 , regeneration 20 (deactivated by acid or fire); __Immunities__ death effects, disease; __Resistances__ poison 15, void 15"
abilities_mid:
  - name: "Wrappings Lash"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the morrigna's web wrappings uses an action to Strike or attempt a skill check"
  - name: "Effect"
    desc: "The morrigna makes a web wrappings Strike against the triggering creature. If the strike is a critical hit, the triggering action is disrupted."
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bo staff_ +31 (Magical, Parry, reach 10 feet, Trip) __Damage__ 2d8+14 bludgeoning plus 4d6 shepherd's touch"
  - name: "Melee"
    desc: "⬻ web wrappings +29 (Magical, reach 10 feet) __Damage__ 3d12+14 bludgeoning plus Grab and 4d6 shepherd's touch"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) A morrigna can take the appearance of any Small or Medium animal or humanoid. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their Strikes deal. Unless they choose to manifest their web wrappings in their new form, they cannot make web wrappings Strikes."
  - name: "Shepherd's Touch"
    desc: "A morrigna's Strikes have the benefit of a _ghost touch_ property rune and deal an additional 4d6 void damage to living creatures or 4d6 vitality damage to undead."
  - name: "Spider Minions"
    desc: "⬽ (Divine, Summon) The morrigna summons a giant tarantula (page 321) or spider swarm. These spiders have the summoned trait and remain for 10 minutes or until reduced to 0 Hit Points, whichever comes first. The morrigna does not need to Sustain the Spell to direct these summoned creatures, and the morrigna can have any number of summoned spiders in existence at once. The morrigna can see through the eyes of any of their summoned spiders at any time."
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 35, attack +30 - __Cantrips (8th)__ Detect Magic, Read Aura, Stabilize, Vitality Lash, Void Warp - __1st__ Bane, Bless, Enfeeble (4 slots) - __2nd__ Calm, See the Unseen, Silence (4 slots) - __3rd__ Blindness, Crisis of Faith, Dream Message (4 slots) - __4th__ Dispelling Globe, Read Omens, Unfettered Movement (4 slots) - __5th__ Dispel Magic, Scouting Eye, Sending (4 slots) - __6th__ Field of Life, Heal, Spirit Blast (4 slots)"
  - name: "Divine Innate Spells"
    desc: "DC 37 - __4th__ Talking Corpse - __Constant (5th)__ Truespeech, Speak with Animals"
  - name: "Rituals"
    desc: "DC 37 - __5th__ Call Spirit"
sourcebook: "_Monster Core_, page 276."
```

```encounter-table
name: Morrigna
creatures:
  - 1: Morrigna
```
