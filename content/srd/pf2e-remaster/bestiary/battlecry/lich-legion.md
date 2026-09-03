---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lich Legion"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Lich Legion"
level: 18
source: "Battlecry!"
aon_id: "creature-3926"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3926"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Lich Legion"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Rare"
trait_02: "Troop"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision"
languages: "Aklo, Chthonian, Common, Diabolic, Draconic, Elven, Necril, Sakvroth"
skills:
  - name: "Skills"
    desc: "Arcana +38, Deception +35, Diplomacy +35, Religion +31, Stealth +29"
abilityMods: [1, 5, 0, 9, 6, 4]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +27; __Ref__: +30; __Will__: +33 +1 status to all saves vs. vitality"
hp: 330
health:
  - name: "HP"
    desc: "330 (4 segments, mass rejuvenation, void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ cold 15, physical 15 (except magical bludgeoning); __Weaknesses__ area damage 15, splash damage 15"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 60 feet, DC 37"
  - name: "Mass Rejuvenation"
    desc: "This functions similarly to a lich's rejuvenation ability, though with all the liches of a legion returning as a troop thanks to a collective soul cage, which is a level 18 item that has Hardness 15 and 54 Hit Points."
  - name: "Troop Counterspell"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the legion's sight casts a spell the legion has prepared"
  - name: "Effect"
    desc: "The lich legion expends a prepared spell to counter the triggering creature's casting of that same spell. The lich legion loses the spell slot as if they had cast the triggering spell. The lich legion then attempts to counteract the triggering spell with a +2 status bonus to the counteract check."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Siphoning Grip"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The lich legion touches all enemies within a 5-foot emanation to drain their life (DC 37 basic Reflex save). The damage depends on the number of actions. For each action the lich legion uses, the legion gains 10 temporary Hit Points that last 1 minute. ⬻ 2d8 void damage ⬺ 4d8+11 void damage ⬽ 6d8+13 void damage"
  - name: "Steady Troop Spellcasting"
    desc: "When the lich legion Casts a Spell, their constituent members combine their efforts into casting a more powerful version of the spell than any one member could achieve alone. When Casting a Spell that has an area of a burst, cone, or line and doesn't have a duration, increase the area of that spell. Add 5 feet to the radius of a burst that normally has a radius of at least 10 feet (a burst with a smaller radius is not affected). Add 5 feet to the length of a cone or line that is normally 15 feet long or smaller, and add 10 feet to the length of a larger cone or line. If a reaction would disrupt the lich legion's spellcasting action, the lich legion attempts a DC 12 flat check. On a success, the action isn't disrupted."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 40, attack +35 - __Cantrips (9th)__ Detect Magic, Frostbite, Message, Shield, Telekinetic Hand - __1st__ Enfeeble (×2), Fleet Step, Grim Tendrils - __2nd__ Blur, False Vitality, Resist Energy, See the Unseen - __3rd__ Blindness, Force Barrage, Locate, Vampiric Feast - __4th__ Dispel Magic, Fire Shield, Fly, Translocate - __5th__ Howling Blizzard (×2), Toxic Cloud, Wall of Ice - __6th__ Chain Lightning (×2), Never Mind, Vampiric Exsanguination - __7th__ Eclipse Burst (×2), Vampiric Exsanguination, Warp Mind - __8th__ Arctic Rift (×2), Desiccate, Earthquake - __9th__ Falling Stars, Massacre, Phantasmagoria"
sourcebook: "_Battlecry!_, page 185."
```

```encounter-table
name: Lich Legion
creatures:
  - 1: Lich Legion
```
