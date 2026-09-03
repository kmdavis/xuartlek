---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Exscinder"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Exscinder"
level: 13
source: "Monster Core 2"
aon_id: "creature-4065"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4065"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Exscinder"
level: "Creature 13"
size: "Huge"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: "Rare"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision"
languages: "Aklo, Chthonian, Diabolic, Draconic, Empyrean, Necril, Sakvroth, Utopian; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Arcana +24, Heaven Lore +26, Intimidation +26, Library Lore +26, Occultism +24, Religion +27, Society +26"
abilityMods: [8, 6, 6, 5, 8, 7]
abilities_top:
  - name: "Items"
    desc: "confiscated texts"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +21; __Will__: +25 +1 status to all saves"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ fear; __Resistances__ fire 10; __Weaknesses__ unholy 10"
abilities_mid:
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 15 to all damage against the triggering damage, and the archon can make a Strike against the enemy."
speed: "30 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ binding chains +27 (Disarm, Finesse, Holy, Magical, Trip) __Damage__ 3d8+11 bludgeoning plus 2d6 fire and censorious lash"
  - name: "Ranged"
    desc: "⬻ blazing sigil +25 (Fire, Holy, Magical, range increment 40 feet, Spirit) __Damage__ 5d6 fire plus 3d6 spirit"
abilities_bot:
  - name: "Spells"
    desc: "DC 33, attack +25 - __Cantrips (7th)__ Light, Message - __1st__ Sure Strike (×3) - __2nd__ Invisibility (at will) - __4th__ Heal (at will), Translocate (at will) - __7th__ Divine Immolation, Interplanar Teleport, Rewrite Memory (at will), Ring of Truth - __Constant (5th)__ Truespeech"
  - name: "Censorious Lash"
    desc: "(Divine, Incapacitation, Mental) When the exscinder hits a creature with a binding chains Strike, that creature must attempt a DC 30 Will save. On a failure, it's controlled by the exscinder for its first action on its next turn (or controlled for its entire next turn on a critical failure)."
  - name: "Change Size"
    desc: "⬻ (Concentrate, Divine, Polymorph) The exscinder changes size to their choice of Huge, Large, Medium, or Small."
  - name: "Temper thy Words"
    desc: "⬻ (Auditory, Concentrate, Divine) The exscinder chooses one written text within 120 feet. They don't need to be able to observe the text, but they can't target one that's deliberately concealed. The exscinder censors the text, modifying it to their wishes. The text can't be referenced, making it useless for functions like Casting a Spell from a scroll, preparing spells from a spellbook, or consulting a scholarly journal. If the text is attended, the creature possessing it can attempt a DC 33 Will save; an unattended text automatically gets a critical failure."
  - name: "Critical Success"
    desc: "The text remains uncensored."
  - name: "Success"
    desc: "The censorship lasts 1 round."
  - name: "Failure"
    desc: "The text is censored for 1 day."
  - name: "Critical Failure"
    desc: "The text is censored permanently. It can be restored only with a _wish_ ritual or similarly powerful magic. Censorship Is... Holy? Censorship is a contentious topic, as it's often used as a method of control. The exscinder has the holy trait, but its actions—censoring and confiscating texts—can be upsetting and even condemnable. Keep in mind, however, that they exist in a world with magical texts that can be deadly when read! This doesn't mean they can't cross the line into actions that mortals consider to be wrong, nor that they might not clash with mortals due to a lack of nuance."
sourcebook: "_Monster Core 2_, page 37."
```

```encounter-table
name: Exscinder
creatures:
  - 1: Exscinder
```
