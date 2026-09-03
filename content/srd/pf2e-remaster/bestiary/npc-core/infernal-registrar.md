---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Infernal Registrar"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Infernal Registrar"
level: 10
source: "NPC Core"
aon_id: "creature-3566"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3566"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Infernal Registrar"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
trait_04: "Unholy"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; (33 to Sense Motive)"
languages: "Common, Diabolic"
skills:
  - name: "Skills"
    desc: "Deception +22, Diplomacy +33, Legal Lore +33, Religion +30, Scribe Lore +30, Society +33"
abilityMods: [2, 2, 2, 5, 3, 4]
abilities_top:
  - name: "Contract Specialist"
    desc: "For encounters involving matters of contracts and dealings with Hell, the infernal registrar is an 18th-level challenge."
  - name: "Death is a Promotion"
    desc: "The infernal registrar does not fear death, as they have a signed infernal contract for immediate promotion to a mid-ranked devil upon their soul's arrival in Hell. They're immune to all Intimidation checks to Coerce involving threats of death."
  - name: "Friends in Low Places"
    desc: "Though devils do not respect most mortals, they respect the office of infernal registrar. No creature with the devil trait of 18th level or lower will knowingly and willingly attack an infernal registrar."
  - name: "Technically Correct"
    desc: "The infernal registrar uses their Legal Lore modifier on all Deception checks to Lie."
  - name: "Items"
    desc: "_staff of office_ (functions as _+1 flaming striking staff_)"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +16; __Will__: +33 +2 circumstance to all saves vs. fear"
hp: 180
health:
  - name: "HP"
    desc: "180; __Resistances__ fire 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff of office_ +19 (Magical, two-hand d8) __Damage__ 2d4+8 bludgeoning plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ fist +18 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
abilities_bot:
  - name: "A Favor for a Favor"
    desc: "⬽ (Concentrate, Divine) The infernal registrar has the authority to make limited infernal contracts with other mortals. They summon a contract with the legal language they desire. Detecting hidden clauses in the contract requires a successful DC 43 Society or a DC 38 Legal Lore check. Once signed, the contract vanishes into the infernal filing system in Hell. The infernal registrar cannot grant any boons beyond their own personal power (usually limited to information, advice, or access to elements of the infernal bureaucracy)."
  - name: "Request Document"
    desc: "⬽ (Concentrate, Divine) The infernal registrar makes a request to summon a copy of any infernal contract a specific creature has signed. They must know enough information to specifically identify the individual who signed. The infernal registrar attempts a Legal Lore check with a DC equal to a hard DC of the level of the creature in question. The infernal registrar will never promise a successful use of this ability in the agreements they make. Each agreement is typically for one attempt. Any copy summoned is simply a copy, has no impact on the original contract if destroyed or altered, and will vanish if taken more than 20 feet from the infernal registrar."
  - name: "Critical Success"
    desc: "A copy of the contract appears before the infernal registrar after 10 minutes."
  - name: "Success"
    desc: "A copy of the contract appears before the infernal registrar after 1 hour."
  - name: "Failure"
    desc: "The attempt fails, but the infernal registrar can try again after 24 hours."
  - name: "Critical Failure"
    desc: "The attempt fails, and the infernal registrar can't try again for the named creature for 1 year. The Devil Out Of The Details Instead of Hell, an infernal registrar might run the bureaucracy of a vast magical city or a commune of otherworldly entities. To represent this, replace any reference to devils with a more appropriate creature type, and replace the registrar's divine spells with arcane or occult spells, respectively. They also speak a more appropriate language, like Draconic or Aklo. Their contract abilities remain essentially the same, though details can be described differently."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21 - __Cantrips (5th)__ Detect Magic, Ignition, Read Aura - __2nd__ Translate (at will) - __3rd__ Chilling Darkness, Fear, Ring of Truth - __4th__ Detect Scrying, Suggestion - __5th__ Banishment, Divine Immolation, Locate"
sourcebook: "_NPC Core_, page 119."
```

```encounter-table
name: Infernal Registrar
creatures:
  - 1: Infernal Registrar
```
