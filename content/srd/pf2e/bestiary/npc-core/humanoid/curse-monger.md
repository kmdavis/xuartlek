---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Curse Monger"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Curse Monger"
level: 14
source: "NPC Core"
aon_id: "creature-3544"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3544"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Curse Monger"
level: "Creature 14"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23"
languages: "Aklo, Chthonian, Common, Daemonic, Fey"
skills:
  - name: "Skills"
    desc: "Arcana +25, Deception +25, Intimidation +23, Occultism +29, Stealth +24"
abilityMods: [1, 5, 3, 8, 4, 4]
abilities_top:
  - name: "Incurable Curse"
    desc: "(curse) The curse monger is permanently clumsy 1, drained 1, enfeebled 1, or stupefied 1 by a curse that can't be removed from them in any way. The GM chooses the condition and decides whether the curse is arcane, divine, occult, or primal."
  - name: "Items"
    desc: "_+1 resilient explorer's clothing_, _+1 striking wounding sickle_, _scroll of fly_"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +23; __Ref__: +25; __Will__: +26 –2 to all saves vs. curses"
hp: 230
health:
  - name: "HP"
    desc: "230"
abilities_mid:
  - name: "Cursed Aura"
    desc: "(aura, curse, occult) 30 feet. The very earth and air around the curse monger are poisoned by the curses that burden their soul. Any creature who enters or starts their turn in the aura must succeed at a DC 31 Will save or be doomed 1 (or doomed 2 on a critical failure). Regardless of the result of its save, the creature is then temporarily immune for 1 hour."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _sickle_ +25 (Agile, Finesse, Magical, Trip) __Damage__ 2d4+13 slashing plus 1d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ fist +24 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+13 bludgeoning"
abilities_bot:
  - name: "Share Burden"
    desc: "⬻ (Concentrate, Curse) The curse monger shares their awful burden with one creature they can see within 120 feet. The target must succeed at a DC 37 Will save or be afflicted with the same condition as the curse monger's incurable curse for 24 hours. On a critical failure, the curse's value is 2. The curse lasts for 24 hours but can be removed (unlike the incurable curse), and ends if the curse monger dies. This action has the same tradition trait as incurable curse. Jinxed Curse Mongers For certain curse mongers, spreading the curse is an involuntary part of the curse itself. When a jinxed curse monger starts their turn, Share Burden automatically attempts to curse a random creature in range that's not already cursed; this doesn't require an action. If the attempt fails, the curse monger must spend their first actions on that turn casting a curse spell (_cursed metamorphosis_, _never mind_, _spellwrack_, _mariner's curse_, _outcast's curse_, or _ill omen_). If the curse monger doesn't want to curse anyone, the GM determines a target at random. The target doesn't have to be an enemy but can't be the curse monger."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 37, attack +29 - __Cantrips (7th)__ Daze, Figment, Telekinetic Hand, Message, Void Warp - __1st__ Bane, Fear, Ill Omen (3 slots) - __2nd__ Darkness, Laughing Fit, Paranoia (3 slots) - __3rd__ Hypercognition, Slow, Mind Reading (3 slots) - __4th__ Blood Vendetta, Outcast's Curse, Vision of Death (3 slots) - __5th__ False Vision, Mariner's Curse, Wave of Despair (3 slots) - __6th__ Never Mind, Phantasmal Calamity, Spellwrack (3 slots) - __7th__ Cursed Metamorphosis, Dominate, Possession (3 slots)"
sourcebook: "_NPC Core_, page 104."
```

```encounter-table
name: Curse Monger
creatures:
  - 1: Curse Monger
```
