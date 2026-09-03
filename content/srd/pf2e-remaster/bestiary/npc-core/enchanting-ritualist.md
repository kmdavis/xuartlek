---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Enchanting Ritualist"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Enchanting Ritualist"
level: 18
source: "NPC Core"
aon_id: "creature-3545"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3545"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Enchanting Ritualist"
level: "Creature 18"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 31
perception:
  - name: "Perception"
    desc: "Perception +31"
languages: "Common, Diabolic, Empyrean, Fey"
skills:
  - name: "Skills"
    desc: "Arcana +34, Diplomacy +31, Deception +35, Nature +34, Occultism +36, Religion +34"
abilityMods: [4, 3, 1, 6, 6, 8]
abilities_top:
  - name: "Ritual Caster"
    desc: "the enchanting ritualist gains a +2 circumstance to skill checks for rituals"
  - name: "Items"
    desc: "_+2 greater striking club_, _greater bands of force_, ornate ritual book"
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +27; __Ref__: +28; __Will__: +33"
hp: 320
health:
  - name: "HP"
    desc: "320; __Resistances__ mental 20"
abilities_mid:
  - name: "Aura of Contentment"
    desc: "(aura, emotion, incapacitation, mental, occult) 30 feet. A creature that enters or starts its turn in the aura must succeed at a DC 38 Will save or lose the desire to do anything except rest and relax. Hostile actions taken against creatures affected by the aura end the effect. If a creature in the aura succeeds on their Will save or is the subject of a hostile action, it's temporarily immune to the aura of contentment for 24 hours. The enchanting ritualist can exempt creatures from the aura's effects."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _club_ +30 (Magical) __Damage__ 3d6+12 bludgeoning plus 2d6 mental and fool's feast"
  - name: "Melee"
    desc: "⬻ fist +28 (Agile, Magical, Nonlethal, Unarmed) __Damage__ 1d4+12 bludgeoning plus 2d6 mental and fool's feast"
  - name: "Ranged"
    desc: "⬻ enchanting wisps +30 (Magical, Mental, range 100 feet) __Damage__ 9d6 mental plus fool's feast"
  - name: "Ranged"
    desc: "⬻ _club_ +28 (Magical, thrown 10 feet) __Damage__ 3d6+12 bludgeoning plus 2d6 mental and fool's feast"
abilities_bot:
  - name: "Fool's Feast"
    desc: "Recipients of the ritualist's generosity pay dearly if the ritualist decides to turn against them. The ritualist gets a +4 circumstance bonus to attack rolls against any creature that has willingly participated in or benefited from one of their spells or rituals conducted in the last 12 hours. A creature that didn't help conduct a ritual still qualifies if it benefited in other ways, such as drinking a serving of _fortifying brew_. When the enchanting ritualist damages such a creature with a Strike, the target is affected by a 9th-rank _cursed metamorphosis_ spell (DC 42). If the Strike was a critical hit, the creature gets a degree of success one worse than it rolled. Once a creature succeeds at a save against this spell, it is temporarily immune for 24 hours."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 42, attack +34 - __Cantrips (9th)__ Daze, Detect Magic, Light, Read Aura, Telekinetic Hand - __1st__ Alarm, Fear, Ill Omen, Illusory Object (4 slots) - __2nd__ Augury, Darkvision, See the Unseen, Status (4 slots) - __3rd__ Dream Message, Hypnotize, Illusory Disguise, Levitate (4 slots) - __4th__ Confusion, Fly, Honeyed Words, Translocate (4 slots) - __5th__ Dreaming Potential, Hallucination, Scouting Eye, Sending (4 slots) - __6th__ Mislead, Repulsion, Truesight, Zealous Conviction (4 slots) - __7th__ Mask of Terror, Project Image, Truespeech, Wave of Despair (4 slots) - __8th__ Canticle of Everlasting Grief, Quandary, Spirit Song, Uncontrollable Dance (4 slots) - __9th__ Foresight, Overwhelming Presence, Synesthesia, Telepathic Demand (4 slots)"
  - name: "Rituals"
    desc: "DC 44 - __2nd__ Heartbond - __3rd__ Geas - __4th__ Atone, Rest Eternal - __5th__ Astral Projection, Fortifying Brew, Call Spirit, Planar Servitor, Resurrect - __6th__ Binding Circle, Commune - __7th__ Collective Memories, Planar Displacement - __9th__ Fantastic Facade"
sourcebook: "_NPC Core_, page 105."
```

```encounter-table
name: Enchanting Ritualist
creatures:
  - 1: Enchanting Ritualist
```
