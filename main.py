from utils import (
    RangedGenerator,
    dict_has_key,
    is_dict,
    get_greater_or_less,
    is_int,
    collect,
)
from beaupy import select
from random import random


story = {
    "main_story": [
        {
            "dialogue": "Cog is a young village boy who migrates to the west seeking a better life.",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "On his journey he encounters a pack of hyenas. What should he do?",
            "options": {
                "Run Away": {
                    "factor": 0.9,
                    "jump_forward_by": {
                        "is_greater_than": 1,  # Index to jump to
                        "is_less_than": "events#death",
                    },  # This determines what to do based off the results of factor
                },
                "Fight": {
                    "factor": 0.4,
                    "jump_forward_by": {
                        "is_greater_than": 2,
                        "is_less_than": "events#death",
                    },
                },
                "Give up": {"jump_forward_by": -1},
            },
        },
        {
            "dialogue": "Cog was able to 'Run Away' from the hyenas",
            "options": {"Next": {"jump_forward_by": 2}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "Cog was able to 'Fight' and escape the hyenas",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },  # I was thinking about making the dialogue dynamic like the death event, but that would lead to too much checking and ugly code
        {
            "dialogue": "As Cog continues his journey, he notices that his rations are running low.\nFortunately there is a berry bush up ahead, though it looks quite strange.\nWhat should he do?",
            "options": {
                "Eat the berries": {
                    "factor": 0.5,
                    "jump_forward_by": {
                        "is_greater_than": 6,  # The index is sort of messed up because of the poison dialogue, I could make it skip those and jump where its supposed to while having a normal index
                        "is_less_than": "events#death|events#poison",
                    },
                },
                "Look for other food": {
                    "factor": 0.8,
                    "jump_forward_by": {
                        "is_greater_than": 5,
                        "is_less_than": "events#death",
                    },
                },
                "Give up": {"jump_forward_by": -1},
            },
        },
        {
            "when": "poison",
            "dialogue": "Cog, as result of the posion, is sluggish and has a low chance of surviving should he continue. What should he do?",
            "options": {
                "Return to village": {"jump_forward_by": -1},
                "Continue": {"jump_forward_by": 1},
            },
        },
        {
            "when": "poison",
            "dialogue": "Cog perseveres despite the poison coursing through his body.",
            "options": {
                "Next": {"jump_forward_by": 1},
                "Quit": {"jump_forward_by": -1},
            },
        },
        {
            "when": "poison",
            "dialogue": "As he continues, Cog begins hallucinating. Suddenly he collapses as his world goes dark",
            "options": {
                "Next": {"jump_forward_by": 1},
                "Quit": {"jump_forward_by": -1},
            },
        },
        {
            "when": "poison",
            "dialogue": "Cog wakes up in a stone house. Confused he looks around, and smiles when he see's the flag of the western empire",
            "options": {
                "Quit": {"jump_forward_by": -1},
            },
        },  # Sorry, I got a lazy here. So getting poisoned is the best way to win lol
        {
            "dialogue": "After sometime, Cog was able to find an apple tree",
            "options": {"Next": {"jump_forward_by": 2}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "Cog survived eating the berries(though not without some significant bowel movement)",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "As Cog progresses further, he sees more a more signs of western civilization",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "A camp appers in the horizon, Cog goes in for a closer look.",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "As Cog draws closer, he begins to get worried as a foul odor permeates the air",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "Suddenly he jumps back with digust as he sees the camp littered with dead bodies.",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "They look as though they had been torn apart by some wild animal.",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "Cog, now scared, is wondering whether he should continue his journey.\n The animal that killed those people could still be out there.\n What should he do?",
            "options": {
                "Return to the village": {"jump_forward_by": -1},
                "Find another route": {
                    "factor": 0.7,
                    "jump_forward_by": {
                        "is_greater_than": 1,
                        "is_less_than": "events#lost",
                    },
                },
                "Continue on current route": {
                    "factor": 0.4,  # It is extremly slim to survive going on the current path
                    "jump_forward_by": {
                        "is_greater_than": 2,
                        "is_less_than": "events#death",
                    },
                },
            },
        },
        {
            "dialogue": "Cog decides to find another route. Though this path is longer, the thought of coming face to face with whatever killed those people, pushes such complaints aside.",
            "options": {"Next": {"jump_forward_by": 4}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "Cog, against all common wisedom, continues on his path",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "As he continues, he hears fearsome sounds echoing throughout the forest",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "But somehow, Cog makes it through and continues on his way",  # Sorry Mr. Jernigan but I don't feel like adding a whole other branch with the animal encounter and I only have 1 day left to finish this
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "As Cog continues, he spots a city up ahead.",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "Cogs excitment begins to grow as he breaks into a sprint towards the city",
            "options": {"Next": {"jump_forward_by": 1}, "Quit": {"jump_forward_by": -1}},
        },
        {
            "dialogue": "As he reaches the city gates, Cog shouts in exubalation as he sees the symbol of the western empire",
            "options": {
                "Quit": {"jump_forward_by": -1}
            },  # I could make it longer but I only have one day left and I don't feel like it lol
        },
    ],
    "events": {
        "death": {
            "dialogue": "Cog died as a result of choosing to '{}'",
            "should_exit": True,
        },
        "poison": {
            "dialogue": "Cog was poisoned as a result of choosing to '{}'",
            "options": {"Next": 1, "Quit": 0},
            "should_exit": False,
        },
        "lost": {
            "dialogue": "Cog becomes lost and dies of starvation as a result of choosing to '{}'",
            "should_exit": True,
        },
    },
}


def run_event(eventObj, params):
    print(eventObj["dialogue"].format(*params))
    if eventObj["should_exit"] is True:
        ask_to_play_again()
    return eventObj["options"][select(list(eventObj["options"].keys()))]


def run_chapter(storyObj):
    print(storyObj["dialogue"])
    selection = select(list(storyObj["options"].keys()), cursor_style="cyan")
    if (selection == None):
        return run_chapter(storyObj) -1

        

    optionObj = storyObj["options"][selection]

    if is_dict(
        optionObj["jump_forward_by"]
    ):  # This means that it requires some randomization in the outcome
        greater_or_less = get_greater_or_less(optionObj["factor"], random())
        result = optionObj["jump_forward_by"][greater_or_less]
        if is_int(result):
            return int(result)
        else:
            if "|" not in result:
                directive, directiveKey = result.split("#")
            else:
                event1, event2 = result.split("|")
                directive, directiveKey = (event1 if random() < 0.5 else event2).split(
                    "#"
                )
        return run_event(story[directive][directiveKey], [selection])
    else:
        return optionObj["jump_forward_by"]


story_main = story["main_story"]

# Old Generator Code
# def get_chapters():
#   next_index = None
#   for i in story_range.get(len(story_main)):
#       yield story_main[i]
#
#       next_index = yield next_index
#
#
#       if next_index:
#           story_range.jump_to(i + next_index)
#           print(story_range.start)
#       else:
#           story_range.jump_to(++i)


def ask_to_play_again():
    print("Thanks for playing!")
    print("Would you like to play again?")
    answer = select(["Yes", "No"], cursor_style="cyan")
    if answer == "Yes":
        __run_story__()
    else:
        exit()


def __run_story__():
    story_range = RangedGenerator(story_main)
    next_index = 0
    for chapter in story_range:
        if dict_has_key( # Technically I could rewrite it the entire story to function like this, build a new branch from the when property, like "when":"Run Away", and it would be a lot more dynamic
            chapter, "when"
        ):  # If I had more than one when dialogue, I would check if the value of when was in a variable event_history
            story_range.set_array(
                collect(story_main, lambda x: dict_has_key(x, "when")), # Collect all dialogues with the when property in order to build a new story
            )

        next_index = run_chapter(chapter)
        if next_index == -1:
            ask_to_play_again()

        story_range.send(next_index)


globals()["__run_story__"] = __run_story__

__run_story__()
