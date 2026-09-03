---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brimorak"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Brimorak"
level: 5
source: "Monster Core"
aon_id: "creature-2896"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2896"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Brimorak"
level: "Creature 5"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, smoke vision"
languages: "Chthonian, Draconic, Empyrean, Pyric; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Deception +11, Religion +10, Stealth +12"
abilityMods: [4, 3, 4, 1, 1, 2]
abilities_top:
  - name: "Extinguishing Aversion"
    desc: "Dousing a brimorak with water, either ordinary water or from a water effect, causes no physical harm to the fiend but deals 3d6 mental damage. Fully immersing the brimorak in water deals 5d6 mental damage per round."
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a brimorak's vision; they ignore the concealed condition from smoke."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +15; __Ref__: +12; __Will__: +10"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ fire; __Weaknesses__ cold iron 5, holy 5"
abilities_mid:
  - name: "Boiling Blood"
    desc: "Each time an adjacent creature deals slashing or piercing damage to the brimorak, the attacker is sprayed with the brimorak's boiling blood, which deals 2d4 fire damage (DC 19 basic Reflex save)."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flaming sword +15 (Magical, Unholy) __Damage__ 2d8+4 slashing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ hoof +15 (Agile, Unholy) __Damage__ 2d4+4 bludgeoning plus 1d6 fire"
abilities_bot:
  - name: "Flaming Weapon"
    desc: "(Divine, Fire) A brimorak's hooves and any weapon they wield burst into flame. They can also Interact to create a sword of fire and steel, which dissolves if it leaves their grip."
  - name: "Frothing Spew"
    desc: "⬺ (Divine, Fire, Unholy) The brimorak spits their boiling blood in a 20-foot line that deals 6d6 fire damage (DC 21 basic Reflex save). Creatures that fail the save also fall prone as they slip in the greasy blood. The brimorak can't use Frothing Spew again for 1d4 rounds."
  - name: "Fume"
    desc: "⬺ (Divine, Fire)"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The brimorak emits a cloud of thick black smoke in a 10-foot burst adjacent to them. The cloud remains for 1 minute. All creatures within the smoke become concealed, and all creatures outside the smoke become concealed to creatures within it. A creature that enters or begins its turn within the smoke it must succeed at a DC 21 Fortitude save or become sickened 1 (sickened 2 on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21 - __Cantrips (3rd)__ Ignition - __3rd__ Dispel Magic, Fireball - __4th__ Translocate"
  - name: "Rituals"
    desc: "DC 21 - __1st__ Demonic Pact"
sourcebook: "_Monster Core_, page 77."
```

```encounter-table
name: Brimorak
creatures:
  - 1: Brimorak
```
