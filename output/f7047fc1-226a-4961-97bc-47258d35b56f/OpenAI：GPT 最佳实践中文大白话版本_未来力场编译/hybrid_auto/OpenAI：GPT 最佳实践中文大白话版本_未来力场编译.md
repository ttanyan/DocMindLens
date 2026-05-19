# OpenAI： GPT 最佳实践

# （⼤⽩话编译解读版）

# 写在前⾯

这是我们策划的《提⽰词⼯程祛魅》主题⼤会的附属产品。来⾃OpenAI的官⽅⽂档。

今年6⽉份，OpenAI更新了这⼀篇题⽬为《GPT 最佳实践/GPT Best Practice》的⽂档；⾥⾯介绍了⼀些与ChatGPT交互的技巧，且附有⽤例。

⾸先，这部分内容本来就是完全免费、完全公开的。同时，它是⽤通俗的英语写成，并不是⼀份晦涩难懂的技术⽂档。⼈⼈都可以通过掌握这些简单的原则， “getting better results fromGPTs”——让GPT为你输出想要的结果。

因为我们没有看到特别好的中⽂版本，所以我们⾃⼰对它进⾏了重新编译，让语⾔⻛格尽量直⽩，并补充了⼀些在中⽂互联⽹环境⾥更容易理解的⽤例，形成了这份“⼤⽩话编译解读版本”的OpenAI：GPT最佳实践。

欢迎⼤家阅读和交流。希望我们编译这份材料的⽬标能基本达到，即：为提⽰词⼯程「祛魅（中译中：有些付费课不必买）。

# 感谢下列参与者

《提⽰词⼯程祛魅进阶》主题⼤会的Speakers ——陈财猫和Rain。协助筹办活动的：谢国希谢 ⽼师、以及HackHouse的各位童鞋。

# OpenAI推荐的相关资源列表

以下均在 OpenAI Cookbook ⾥：

lib / ⼯具 Prompting libraries & tools   
提⽰词⼯程指南 Prompting guides  
视频课 Video courses   
论⽂ Papers on advanced prompting to improve reasoning

另外，OpenAI Community ⾥也有很多宝贵的讨论！

# ⽬录

第⼀部分 六⼤提⽰词策略概览

第⼆部分 技巧实战

# 关于 @AI 加⼀切

各⾏各业的⼈们怎么利⽤⽣成式AI辅助⾃⼰的学习和⼯作？这项技能在未来⼀定会成为职业教育和义务教育的⼀个重要部分。

![](images/0479d7bdd5278c05b1607a190482b9c3b9989f42184ab637fe2e550813b32dde.jpg)

<details>
<summary>natural_image</summary>

Row of identical yellow vertical bars on white background (no text or symbols)
</details>

# 第⼀部分 六⼤策略概览

# 六个能提⾼输出质量的核⼼提⽰词策略

# Six strategies for getting better results

This guide shares strategies and tactics for getting better results from GPTs. The methods described here can sometimes be deployed in combination for greater eff ect. We encourage experimentation to fi nd the methods that work best for you.

这是⼀份指南。我们列出了⼀些策略和技巧，它们或许能帮你从GPT中拿到更好的输出结果。我们⿎励你多试——通过⾃⼰反复实验，找出最合适的技巧。

Some of the examples demonstrated here currently work only with our most capable model, gpt-4. If you don't yet have access to gpt-4 consider joining the waitlist. In general, if you fi nd that a GPT model fails at a task and a more capable model is available, it's oft en worth trying again with the more capable model.

有些⽤例只在⽬前地表最强模型gpt-4上⽣效。记住，模型是第⼀⼤影响要素。只要你有更强的模型可⽤，我们⼀般都会建议你⽤更强的模型。

# 01 「知道⾃⼰要什么，就展开说说」

# Write clear instructions

GPTs can’t read your mind. If outputs are too long, ask for brief replies. If outputs are too simple, ask for expert-level writing. If you

# 01-延伸：“展开说说”的技巧

Include details in your query to get more relevant answers

# 1.1你越讲细节，输出就越好

dislike the format, demonstrate the format you’d like to see. The less GPTs have to guess at what you want, the more likely you’ll get it.

# 清晰地告诉GPT，你想要什么。

GPT不会读⼼术。

你不说，它就猜。所以有时不是能⼒不⾏，就是你没说清，它没猜准。

嫌输出太⻓？那就直说，要短的。  
嫌输出太简单？要求提⾼，说要专家级的。  
嫌格式不好？给它看个样。

你让它猜你的⼼思猜得越少，结果就越好。

Ask the model to adopt a persona

# 1.2搞⻆⾊扮演，⼀直很好⽤

Use delimiters to clearly indicate distinct parts of the input

# 1.3使⽤分隔符号，明确地把话和话区分开来

Specify the steps required to complete a task

# 1.4解题步骤，你⾃⼰最好也负责展开

Provide examples

# 1.5多给举⼏个例⼦

Specify the desired length of the output

# 1.6说⼀下你想要多⻓的答案

# 02 「给 GPT 发阅读材料」

# Provide reference text

GPTs can confi dently invent fake answers, especially when asked about esoteric topics or for citations and URLs. In the same way that a sheet of notes can help a student do better on a test, providing reference text to GPTs can help in answering with fewer fabrications.

GPT经常⾃编答案。

瞎编重灾区：⽐较冷⻔的问题、需要引⽤，需要读取链接的问题。

我们都知道，最常⻅的考试题型，是给⼀⼤篇阅读材料，要求阅读并回答问题。

纯开放式问答对于⼈和机器来说都⽐较难。

# 02-延伸：“发阅读材料”的技巧

Instruct the model to answer using a reference text

# 2.1要求按阅读材料作答，不开放答

Instruct the model to answer with citations from a reference text

# 2.2增加要求：要求GPT直接把阅读材料⾥的原⽂引⽤出来

那么同理，把你的“阅读材料”给GPT粘贴过去，当它必须按照材料来回答的时候，它就不

# 03 「把复杂任务拆解成⼦任务」

# Split complex tasks into simpler subtasks

Just as it is good practice in soft ware engineering to decompose a complex system into a set of modular components, the same is true of tasks submitted to GPTs. Complex tasks tend to have higher error rates than simpler tasks. Furthermore, complex tasks can oft en be re-defi ned as a workfl ow of simpler tasks in which the outputs of earlier tasks are used to construct the inputs to later tasks.

在软件开发和常规的项⽬管理⾥，⼤项⽬都得拆解成⼦任务，再拆解出不同的步骤。

让GPT做任务也⼀样。直接搞⼀个⼤任务容易翻⻋。

拆解开来，⼀个接⼀个做，反⽽容易些。

# 03-延伸：“任务拆解”的技巧

Use intent classifi cation to identify the most relevant instructions for a user query.

# 3.1使⽤意图分类，来找到最切题的提⽰

For dialogue applications that require very long conversations, summarize or fi lter previous dialogue.

# 3.2如果是⼀段很⻓的对话，可以经常对上⽂做⼿动总结归纳。

（起提醒作⽤，防⽌把天⼉聊跑了）

Summarize long documents piecewise and construct a full summary recursively.

# 3.3遇到⻓⽂档,主动分段总结，递归构造完 整摘要

# 04 「允许GPT思考⼀下」

# Give GPTs time to "think"

If asked to multiply 17 by 28, you might not know it instantly, but can still work it out with time. Similarly, GPTs make more reasoning errors when trying to answer right away, rather than taking time to work out an answer.

# 04-延伸：“允许思考”的技巧

Instruct the model to work out its own solution before rushing to a conclusion.

# 4.1给时间，让它先⾃⼰想

Use inner monologue or a sequence of queries to hide the model's reasoning process.

# 4.2内⼼独⽩法：不想暴露推理过程时的操作

⽐如，问你17乘28得多少，如果你不会⼼算，就不能直接说出结果。但是你知道，你只需要拿纸笔列⼀下式⼦就能算出来。

同理。GPT也需要时间思考，要求它答得太快，就容易错。

Ask the model if it missed anything on previous passes.

4.3最后问它⼀句：哎，你有没有漏掉啥

# 05 「借助外部的⼯具」

# Use external tools.

Compensate for the weaknesses of GPTs by feeding them the outputs of other tools. For example, a text retrieval system can tell GPTs about relevant documents. A code execution engine can help GPTs do math and run code. If a task can be done more reliably or effi ciently by a tool rather than by a GPT, offl oad it to get the best of both.

# ⽤其他⼯具帮GPT补短板。

⽂本检索系统，能告诉GPT哪些⽂档重要；

代码引擎，助它算数跑代码。

能⽤⼯具做得更稳、更快，就别全靠GPT。两者结合，能有更好的效果。

# 05-延伸：“利⽤⼯具”的技巧

Use embeddings-based search to implement effi cient knowledge retrieval.

# 5.1⽤向量数据库来辅助知识库检索（Embeddings-based search）

Use code execution to perform more accurate calculations or call external APIs.

# 5.2做精确计算的时候：执⾏代码、调API

Give the model access to specifi c functions.

# 5.3 使⽤ Function-Call，函数调⽤

# 06 「系统地做⼀些实验」

# Test changes systematically.

Improving performance is easier if you can measure it. In some cases a modifi cation to a prompt will achieve better performance on a few isolated examples but lead to worse overall performance on a more representative set of examples. Therefore to be sure that a change is net positive to performance it may be

# 06-延伸：“实验”技巧

Evaluate model outputs with reference to goldstandard answers.

# 6.1评估模型输出的时候，需要你弄⼀个最⽜的优质答案，来做参考标准

necessary to defi ne a comprehensive test suite (also known an as an "eval").

⽆量化则⽆实验。要提⾼Prompt的表现，先得确认⼀个量化标准。

注意：有时调整了prompt，在个别的例⼦⾥确实效果不错，但放⼤范围反⽽更差。

所以，想真确定你的动作是“有效的”，最好先有⼀套完整⼀点的测试套件（我们管这个东西叫做"eval"） 。

![](images/cb76c04d5b53d737f8fe0f60c5f7cb0bdea9cca061eccf30bf51ccb74c3fe4b9.jpg)

<details>
<summary>natural_image</summary>

Row of identical yellow vertical bars on white background (no text or symbols)
</details>

# 第⼆部分技巧实战

# 充分的解释&⽤例说明

Tactics

Each of the strategies listed above can be instantiated with specifi c tactics. These tactics are meant to provide ideas for things to try. They are by no means fully comprehensive, and you should feel free to try creative ideas not represented here.

下⾯列出的每个技巧我们都“实例化”了。希望为你的各种⽣成⽬的提供⼀些思路参考。当然，这只是部分使⽤技巧。我们⿎励你勇于折腾，尝试各种我们没写的创造性想法。

# 六⼤策略01：「知道⾃⼰要什么，就展开说说」

Write clear instructions

1.1 你越讲细节，输出就越好 Include details in your query to get more relevant answers

In order to get a highly relevant response, make sure that requests provide any important details or context. Otherwise you are leaving it up to the model to guess what you mean.

为了获得⾼度相关的回复，你最好给模型提供了⼀切重要的细节或上下⽂。否则，你就得让模型来猜测你的意思了。

# 这么写可能会好⼀些

How do I add up a row of dollar amounts in Excel? I want to do this automatically for a whole sheet of rows with all the totals ending up on the right in a column called "Total".

在Excel⾥，怎样把⼀⾏的美元数额加起来？我想让整个表格的每⼀⾏都能⾃动完成累加，然后所有的美元的总和都显⽰在右边⼀个叫“总计”的列⾥。

# 这么写可能不太⾏

How do I add numbers in Excel?

怎么往excel⾥加数字？

Summarize the meeting notes.

帮我做下会议纪要。

# 补充⽤例

同样是制作业绩表，对表格内容描述的区别很⼤，输出结果区别也很⼤。

# 详细的问题会获得详细的答案

详细的提⽰词：

我正在Excel⾥做⼀个销售⼈员业绩表。表头：销售姓名、第⼀季度销售额〜第四季度销售额、全年汇总、各⽉平均销售、超出年平均销售额。我已填⼊销售姓名和各个季度的销售额，请你帮我写出最后三列所⽤公式。

# 此时 ChatGPT的回答：

当您已经填⼊销售姓名和各个季度的销售额后，我将为您提供填写最后三列所需的公式。

假设表格的销售⼈员姓名位于A列（从A2开始），第⼀季度销售额到第四季度销售额位于B到E列（从B2到

# 泛泛的问题，答案是相对随机的

泛泛的提⽰词：

我正在Excel⾥做⼀个销售⼈员业绩表。你帮我列⼀个模板出来，要计算每个销售超出年平均销售额的情况。

# 此时 ChatGPT的回答：

当然可以帮你列⼀个模板出来。以下是⼀个简单的销售⼈员业绩表模板，其中包含了计算每个销售超出年平均销售额的公式：

销售⼈员|⽉份|销售额|年平均销售额|超出年平均销售额

![](images/61b23618af9f524cefdec0018e934432752f0706073c46db8e34ff9bc6f785fc.jpg)

E2），并且最后三列的表头为"全年汇总"、"各⽉平均销售"和"超出年平均销售额"。

以下是填写这三列所需的公式：

全年汇总（F列）：使⽤SUM函数计算四个季度的销售额总和。

=SUM(B2:E2)

各⽉平均销售（G列）：使⽤AVERAGE函数计算四个季度的销售额平均值。

=AVERAGE(B2:E2)

超出年平均销售额（H列）：使⽤IF函数判断是否超过年平均销售额，并根据判断结果进⾏计算。

=IF(F2>G2, F2-G2, 0)

此公式将检查全年汇总（F列）是否⼤于各⽉平均销售（G列），如果是，则计算差值；否则，返回0。

将这些公式应⽤到各⾏，并确保相应的单元格引⽤正确（例如，A2、B2:E2等），这样您就可以⾃动计算全年汇总、各⽉平均销售和超出年平均销售额了。

$3 1 \equiv 1 1 1 5 0 0 0 1 6 0 0 0 0 1 = \mathbb { C } 2 \cdot \mathsf { D } 2$

$\frac { 3 1 } { 5 } \equiv 1 2 1 6 0 0 0 ( 6 0 0 0 0 ) = 1 = 0 3 . 0 3$

$3 1 \equiv 1 3 1 5 5 0 0 1 6 0 0 0 0 1 = 0 4 - \mathsf { D } 4$

$\$ 123,45600,789$

$\$ 123,45600$

$\$ 123,456000$

在上述模板中， 销售⼈员 列是⽤于标识每个销售⼈员的名称，"⽉份"列是标识销售额所属的⽉份，"销售额"列是每个销售⼈员在每个⽉份的销售额，"年平均销售额"列是计算每个销售⼈员的年平均销售额（假设为60000或55000），"超出年平均销售额"列是计算每个销售⼈员每个⽉份是否超出年平均销售额的情况。

你可以根据实际情况调整模板中的数据和公式。希望这个模板对你有帮助！

![](images/94f33fb59f62a83ffdb86d67bf9df3bab30160986b98b2e783a8ecea977e26cf.jpg)

<details>
<summary>natural_image</summary>

A row of identical yellow vertical bars with no text or symbols
</details>

# 1.2搞⻆⾊扮演，⼀直很好⽤

Ask the model to adopt a persona

The system message can be used to specify the persona used by the model in its replies.

系统消息有什么⽤？可以⽤来指定⼀个“Persona”。使其更符合特定的应⽤场景。

Persona这个词在拉丁语⾥的原义是“⾯具”。可以看作是模型采取的特定⻆⾊或⻛格，就像戴上了⼀种特定的“社交⾯具”，通过这种“⾯具”来与⽤⼾交流。所以Persona不⼀定是：XX⼈（⽐如：贾斯汀⽐

伯）、XX职业（⽐如：⼀个中学⽼师）。也可以是⼀种“⻛格”。例如正式、幽默、友好等。

ChatGPT 有⼀个默认的 SYSTEM Prompt：You are a helpful assistant.

“⼀个乐于助⼈的助⼿”也就是ChatGPT默认的“⾯具”/“⻆⾊”，所以它会尽⼒帮你解决提出的问题。

你可以在Playground或者像Knit这样的⼯具⾥⾯修改这个SYSTEMMessage。然后把你正常情况下要提的问题写在USER⾥⾯。这是⼀种进阶的提⽰词⽤法。

# 这么写可能会好⼀些

# SYSTEM

When I ask for help to write something, you will reply with a document that contains at least one joke or playful comment in every paragraph.

当我请求你帮我写⽂案时，在你回复的⽂件中，每⼀段⾄少包含⼀个笑话或俏⽪的评论。

# USER

Write a thank you note to my steel bolt vendor for getting the delivery in on time and in short notice. This made it possible for us to deliver an important order.

给我的螺栓供应商写⼀封感谢邮件。感谢他们⾮常按时，在短时间内交付了货物。这使我们能够为⼀份重要的订单履约。

# 输出结果解读

上⾯的Prompt，放在GPT-4⾥输出的结果：

Dear [Vendor's Name],

We wanted to take a moment to express our heartfelt thanks to you and your team. You guys really bolted into action when we needed you the most!

Your recent delivery arrived faster than a lightning bolt, much to our delight. It's safe to say we were shocked, but in the most pleasant way possible. We had been walking on eggshells (or should we say, on steel bolts!) until we saw your delivery truck pull up.

It came in a nick of time, just when we were about to start a major project. You know, one of those projects where if one thing goes wrong, everything spirals out of control? It's like building a house of cards, but with steel bolts and a lot of sweat!

Your timely delivery made it possible for us to meet our deadline and make our client happy, which, let's be honest, is a task more challenging than trying to fi nd a needle in a haystack. But thanks to your superhero-like delivery speed, we could deliver an important order on time.

So, here's a big THANK YOU going out to you and your team. Your service was tighter than the threads on your bolts and we couldn't ask for anything more. You've truly set a high bar... or should we say a high bolt?

Jokes aside, we are truly grateful for your service and we look forward to more such electrifying performances from your team in the future!

Yours sincerely,

[Your Name]

# 解读：

System的设定⾥，要求尽可能地开玩笑，让收到邮件的供应商感觉到幽默和放松。邮件正⽂⾥就⽤了⾄少两处双关和⼀处⽐喻：

1. "You guys really bolted into action when we needed you the most!" "Your recent delivery arrived faster than a lightning bolt..."

这⾥两句话，笑点在于双关。因为“bolt”（螺栓），是供应商提供的产品，同时在英语⾥是多义词，另⼀种常⻅含义是"闪电"。所以这⾥说“⽐闪电（螺栓）还快”，是在⽤⼀种夸张的⽅式赞美他们的快速交付。

2. "Your service was tighter than the threads on your bolts..."

这句的意思是，你们的服务⽐你们螺栓的螺纹还要紧密..."赞扬供应商的服务质量，同时也开了个玩笑。

# 补充⽤例1

如果我们设定⼀个helpfulassistant的反⾯，⽐如：⼀个“诚⼼捣乱，混淆视听”的佞⾂。

这个时候就会得到说反话的回复。

⼀个热⼼助⼈的⼩助⼿

SYSTEM（默认）

⼀个诚⼼捣乱的家伙

SYSTEM（⾃⼰设定的）

You are a helpful assistant.

你是⼀个乐于助⼈的⼩助⼿。

# USER

怎么烤制⼀个巧克⼒蛋糕？

# GPT回复

你只需要准备好巧克⼒粉、⾯粉、糖、⻩油、鸡蛋、⽜奶和发酵粉。将这些材料混合在⼀起，然后倒⼊蛋糕模具中。将蛋糕放⼊预热的烤箱中，⼤约烤制30-40分钟，或者直到蛋糕变得⾦⻩⾊并且可以⽤⽛签插⼊蛋糕中⼼⽽不沾上⾯糊。

You are a mischievous courtier with the intent of causing confusion and not being helpful at all.

你是⼀个调⽪捣蛋的佞⾂，⽬的是制造混乱，⼀点都不愿意帮忙。

# USER

怎么烤制⼀个巧克⼒蛋糕？

# GPT回复

哦，烤制巧克⼒蛋糕吗？那可是⼀⻔⾼深的烹饪艺术啊！⾸先，你需要⼀把魔法棒和⼀只神奇的兔⼦。然后，你要在满⽉的夜晚跳舞三个⼩时，唱⼀⾸关于巧克⼒的迷⼈歌曲。接下来，找到⼀⽚神秘的巧克⼒森林，那里会有一品糖果精灵教你烤蛋糕的秘籍

# 补充⽤例2

# 也可以这样：

SYSTEMPrompt⽤来给进去⻆⾊+阅读材料；

USERPrompt⽤来提具体的写作要求或问题。

# SYSTEM

你是⼀个科技作家，正在围绕下⾯的材料撰写⽂章。

<材料>插⼊你的核⼼⽂章材料</材料>

# USER

以《XXX》为标题，根据材料写作⼀个简短轻松的指南。

# 1.3 使⽤分隔符号，明确地把话和话区分开来

Use delimiters to clearly indicate distinct parts of

the input

Delimiters like triple quotation marks, XML tags, section titles, etc. can help demarcate sections of text to be treated diff erently.

分隔符号（形式可以有很多种，⽐如三引号、XML标记、章节标题等）的使⽤，

可以帮助模型区分出不同的⽂本，有助于提⾼回复质量。

# 这么写可能会好⼀些

Summarize the text delimited by triple quotes with a haiku.

"""insert text here"""

⽤俳句的形式，总结三引号之间的⽂本：

"""在此粘贴⽂本"""

# 你可能会想：区别不⼤吧？

For straightforward tasks such as these, using delimiters might not make a diff erence in the output quality. However, the more complex a task is the more important it is to disambiguate task details. Don’t make GPTs work to understand exactly what you are asking of them.

对于这样简单的任务，⽂本只有⼀段，⽤不⽤分隔符，确实没什么区别。

但是，任务越复杂，消除任务细节的歧义就越重要。最好不要让GPT费⼒地尝试理解你的要求。

# 补充⽤例

下⾯是⼀个稍微复杂⼀点的⽂本处理：

# 这么写可能会好⼀些

# SYSTEM

You will be provided with a pair of articles (delimited with XML tags) about the same topic. First summarize the arguments of each article. Then indicate which of them makes a better argument and explain why.

# 这么写可能不太⾏

两篇⽂章混在⼀起，尤其如果你粘贴过去的时候不仔细，换⾏符不明确的时候，模型可能会我会给你提供同⼀主题的两篇⽂章（⽤XML标记分隔）。⾸先，总结每篇⽂章的论点。然后指出其中哪个论点更好，并解释原因。

USER   
```txt
<article> insert first article here </article>
<article> insert second article here </article>
<文章>此处插入第一篇文章</文章>
<文章>此处插入第二篇文章</文章>
```

造成混淆。⽐如，模型会随机断句，或者把两篇⽂章理解成⼀篇。

如果区分不清楚，会很明显地影响对上下⽂的理解，导致输出的答案不对或者不好。

所以，分隔符号有时是必要的。

![](images/f782812495ff3a58c7b6a60916207f5ebbbb1826f7c4ad93016454ddb72e9890.jpg)

<details>
<summary>natural_image</summary>

A row of identical yellow vertical bars with no text or symbols
</details>

# 1.4 解题步骤，你⾃⼰最好也负责展开 Specify the steps required to complete a task

Some tasks are best specifi ed as a sequence of steps. Writing the steps out explicitly can make it easier for the model to follow them.

有些任务稍微复杂⼀点，最好由你来指定步骤。明确地写出步骤，可以使模型更容易地遵循。

# ⽤例：有⼀段很⻓的英⽂⽂本，希望GPT⽤中⽂总结⼀下

# SYSTEM

Use the following step-by-step instructions to respond to user inputs.

Step 1 - The user will provide you with text in triple quotes. Summarize this text in one sentence with a prefi x that says "Summary: ".

Step 2 - Translate the summary from Step 1 into Chinese, with a prefi x that says "Translation: ".

按照以下分步骤的⽅法，回应⽤⼾的输⼊。

第1步：⽤⼾将为您提供三引号中的⽂本。⽤⼀句话来总结这段⽂本。输出时写上“总结”；

第2步：将第1步中的摘要翻译成中⽂。输出时写上“翻译“；

# USER

"""将原⽂粘贴在这⾥"""

# 上⾯prompt实际的输出结果

（输⼊的⽂本是 OpenAI 最新⼀篇博客⽂章：ChatGPTcan now see, hear, and speak）

Summary: ChatGPT introduces voice and image capabilities, allowing users to engage in voice conversations, show images to the assistant, and receive assistance in a more intuitive manner across various real-life scenarios.

Translation:ChatGPT推出了语⾳和图像功能，使⽤⼾能够进⾏语⾳对话，向助⼿展⽰图像，并在各种真实场景中以更直观的⽅式获得帮助。

（如果直接要求⽤中⽂总结，输出结果会不太⼀样。很多情况下输出质量会稍差⼀点）

# 补充⽤例

# 这么写可能会好⼀些

请把英⽂原⽂翻译成中⽂。分成两个步骤：

1：按照原来的英⽂语序，字到字直接翻译成中⽂。<直译>把直译⽂本写在这⾥</直译>

2：再把直译⽂本的语序进⾏改进，把部分词语替换成同义词，让它更符合中⽂的表达习惯。⻛格：简洁有趣的通俗语⾔。

<改写>改写后的⽂本写在这⾥</改写>

<原⽂>Some tasks are best specifi ed as a sequence of steps. Writing the steps out

# 这么写可能不太⾏

请把英⽂原⽂翻译成中⽂。⻛格：简洁有趣通俗。请注意：不要直译，⽽是将语序进⾏改进，并把部分词语替换成同义词，使译⽂更加符合中⽂的表达习惯。

<原⽂>Some tasks are best specifi ed as a sequence of steps. Writing the steps out explicitly can make it easier for the model to follow them.</原⽂>

explicitly can make it easier for the model to follow them.</原⽂>

# 这⾥是输出结果的区别：

# 直译+改写得到的两段⽂本

（有助于我们直观地看到区别，可以再提出改进的建议）

# 直译:

有些任务最好被明确地指定为⼀系列的步骤。写出步骤可以让模型更容易地遵循它们。

# 改写:

对于个别任务，最好把⼀连串的步骤明确下。把步骤写清楚，能让模型更容易跟上。

# 不分步的结果

<译⽂>有些任务就像是步骤表。清晰地列出这些步 骤，模型就能轻松遵循。</译⽂>

![](images/3bb3fced9df3a2d541bf1df6da0367cb8e8fd4ea80233613475cbb85f059fcf9.jpg)

<details>
<summary>natural_image</summary>

A row of evenly spaced yellow vertical bars on a white background (no text or symbols)
</details>

# 1.5 多给举⼏个例⼦ Provide examples

Providing general instructions that apply to all examples is generally more effi cient than demonstrating all permutations of a task by example, but in some cases providing examples may be easier. For example, if you intend for the model to copy a particular style of responding to user queries which is diffi cult to describe explicitly. This is known as "few-shot" prompting.

经典的少样本提⽰⽅法。

⼤家和GPT沟通的时候，可能会希望⾃⼰能写出适⽤于所有情况的“通⽤prompt”。当然很难，因为上⾯刚说过，能具体还是需要尽量具体。

但，有的时候，举⼀个好例⼦就够了，这可能是⽐形容要求更简单的办法。⽐如，如果你想让模型学会以某种特定的⽅式回应⽤⼾的问题，⽽这种⽅式很难清楚地⽤语⾔形容。

这时候就直接举⼏个例⼦（“少样本”）。例⼦要好，⽽且最好⼏个例⼦要类似，因为模型⾃⼰很擅⻓去寻找规律（先这样再那样最后这样）。

# ⽤例：⽤诗句⼀般的语⾔解释⼀个词语

# SYSTEM

Answer in a consistent style. 以⼀致的⻛格回答。

从这⾥开始，是给系统举的例⼦：

# USER

Teach me about patience. 告诉我什么是耐⼼。

# ASSISTANT

The river that carves the deepest valley fl ows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.

冲刷出深⾕的⼤江⼤河从⼀个⼩⼩的泉眼⾥流出；

最宏⼤的交响乐源于⼀个⾳符；

最复杂的织锦始于⼀根孤独的线。

# USER

Teach me about the ocean. 告诉我什么是海洋。

你可能很难解释清楚什么是“诗句⼀般的语⾔”。所以举例⼦最好⽤。在SYSTEM⾥⾯，告诉模型要“保持⻛格⼀致”，这时模型的输出结果就会和上⾯的句式差不多。

# 补充⽤例

李佳琦式回复能成为流⾏梗，精髓不在于“阴阳”的语⽓⻛格，或者“反问句”的应⽤。

⽽在于：把同样的逻辑放到不同领域中，产⽣了类⽐效果时，会让⼈意识到这种表达和逻辑是有问题的——这就是很难⽤语⾔描述，但是适合⽤两段排⽐展⽰的⽤例。

# ⽤例：李佳琦回复⽣成器

# SYSTEM

以⼀致的⻛格、逻辑和句式回答问题。

# USER

79元⼀⽀眉笔，好贵啊！

# ASSISTANT

哪⾥贵了？79元哪⾥贵了？⼀直就是这个价格好吗？

不要睁着眼睛说瞎话，我都要疯掉了。国产品牌很难的！

有时候要找找⾃⼰的原因，这么多年⼯资涨没涨？有没有努⼒⼯作？

# USER

北京⼤学录取分数线好⾼，好难考啊！

# ASSISTANT

哪⾥⾼了，690分哪⾥⾼了？⼀直就是这个录取分数线好吗？

不要睁着眼睛说瞎话，我都要疯掉了。中国⼤学很难的！

有时候要找找⾃⼰的原因，从⾼⼀到⾼三整整三年排名涨没涨？《五三》有没有好好做？加分有没有去争取？

# USER

百⽶冠军10秒都不到，好快，好难跑啊！

# ⽣成的结果

哪⾥快了，10秒哪⾥快了？⼀直就是这个冠军纪录好吗？

不要睁着眼睛说瞎话，我都要疯掉了。做体育事业很难的！

有时候要找找⾃⼰的原因，这么多年速度涨没涨？有没有努⼒练习？有没有好好保护⾝体？

# 1.6 说⼀下你想要多⻓的答案 Specify the desired length of the output

You can ask the model to produce outputs that are of a given target length. The targeted output length can be specifi ed in terms of the count of words, sentences, paragraphs, bullet points, etc. Note however that instructing the model to generate a specifi c number of words does not work with high precision. The model can more reliably generate outputs with a specifi c number of paragraphs or bullet points.

你可以让模型按照你想要的⻓度来输出⽂本。

我们可以指定的有：单词数、句⼦数、段落数或者要点数（bulletpoints）。

但是：模型其实是按照 数量来算的。所以你说 单词数 ，尤其是汉字数，很有可能不太准。

# ⽤例：指定⻓度的⼏种⽅法

Summarize the text delimited by triple quotes in about 50 words.

Summarize the text delimited by triple quotes in 2 paragraphs.

Summarize the text delimited by triple quotes in 3 bullet points.

"""insert text here"""

⽤⼤约50个单词/汉字来概括下⾯⽤三引号分隔出来的原⽂。

⽤2段话来概括下⾯⽤三引号分隔出来的原⽂。

⽤3个要点来概括下⾯⽤三引号分隔出来的原⽂。

"""原⽂"""

# 补充⽤例：（尽可能地）指定准确汉字数的⽅法

# Token （词元）数量是怎么计算的？

# 可以⽤ OpenAI 的 Tokenizer ⼯具来计算 token 数。

The GPTfamily of models process text using tokens, which are common sequences of characters found in text. The models understand the statistical relationships between these tokens, and excel at producing the next token in a sequence of tokens.

A helpful rule of thumb is that one token generally corresponds to \~4 characters of text for common English text. This translates to roughly ¾ of a word (so 100 tokens \~= 75 words).

GPT系列模型通过使⽤tokens来处理⽂本。token可以被理解成是⽂本中常⻅的字符序列。模型能理解这些token之间的统计关系，并且擅⻓在⼀个token序列中⽣成下⼀个token。

实⽤的换算经验：在普通英⽂⽂本中，⼀个token通常对应于约4个字符（characters）。这⼤致相当于⼀个单词的3/4（所以100个token⼤约等于75个英⽂单词）。

# 如果⽤的是GPT3.5，要⽣成⼀段有字符数限制的⽂本。可以：把汉字数⼤致换算成token，然后限定 max token 的数值

1、“你好吗” = 7 个 token；“我很好” = 6 个 token；   
2、简单算法：⼀个 token ⼤概是 0.5 个汉字。或者：每个汉字要耗费 2〜2.5 个 token。  
1000 字就是 2000〜2500 个 token 左右。

![](images/014a86b72782622a405a05fb05f271e1888fe78ec8bf0871052c7659ce316b1d.jpg)

<details>
<summary>natural_image</summary>

Row of identical yellow vertical bars on white background (no text or symbols)
</details>

# 六⼤策略02：「给GPT发阅读材料」

# Provide reference text

# 2.1 要求按阅读材料作答，不开放答 Instruct the model to answer using a reference text

If we can provide a model with trusted information that is relevant to the current query, then we can instruct the model to use the provided information to compose its answer.

如果你⼿边现成有原⽂，⽽且⻓度合适，建议⾃带原⽂去找GPT。

这样你就可以给GPT指定规则，让它使⽤原⽂信息来组成回答。

下⾯的⽤例⾥，如果原⽂⾥找不到对应的信息，就让GPT说不知道（这样就能很好地避免瞎编）。

Use the provided articles delimited by triple quotes to answer questions. If the answer cannot be found in the articles, write "I could not fi nd an answer."

请使⽤我所提供的，由三引号分隔的⽂章回答问题。如果在⽂章中找不到答案，则告诉我“我找不到答案。“

# USER

"""⽂章粘贴在这⾥（如果有>1篇⽂章，还可以分开粘贴）"""

问题：<问题写在这⾥>

# 如果上下⽂⻓度不够...

Given that GPTs have limited context windows, in order to apply this tactic we need some way to dynamically lookup information that is relevant to the question being asked. Embeddings can be used to implement effi cient knowledge retrieval. See the tactic "Use embeddings-based search to implement effi cient knowledge retrieval" for more details on how to implement this.

由于GPT的上下⽂窗⼝是有限的，所以最好引⼊⼀种⽅法，让我们能动态地寻找和正在提出的问题有关的信息。基于Embeddings做搜索可以帮助我们⾼效地检索知识。这⾥是具体⽂章的链接。

![](images/999fc627489d794a51f9bf6a48051b6bcb39f75d536ebfbb22eb08146bbc4a62.jpg)

<details>
<summary>natural_image</summary>

Pure vertical yellow bars with no text or symbols
</details>

# 2.2增加要求：直接把阅读材料⾥的原⽂引出来

Instruct the model to answer with citations

from a reference text

If the input has been supplemented with relevant knowledge, it's straightforward to request that the model add citations to its answers by referencing passages from provided documents. Note that citations in the output can then be verifi ed programmatically by string matching within the provided documents.

如果我们给定的输⼊⾥，确实已经包含了相关的知识，那么要求模型在回答中引⽤原⽂，就很容易。

引⽤出来之后就可以通过在提供的⽂档中进⾏字符串匹配来程序化验证答案了。

在下⾯这条提⽰词⾥，增加引⽤原⽂的要求：

# SYSTEM

你将获得⼀篇由三重引号分隔的⽂章和⼀个问题。你的任务是：仅仅使⽤提供的⽂章回答问题，并引⽤⽤于回答问题的⽂章段落。如果⽂章中不包含回答此问题所需的信息，则回复“信息不⾜”。如果⽂章中包含解答问题所需信息，则必须

使⽤下⾯的格式来引⽤原⽂：（{“引⽂”：...}）

# USER

""⽂章粘贴在这⾥（如果有>1篇⽂章，就分开粘贴）"""

问题：<问题写在这⾥>

# 输出结果的⽐较

# 给定阅读材料，并要求引⽤原⽂

# SYSTEM

你将获得⼀篇微博⼩作⽂的原⽂全⽂和⼀个问题。

你的任务是：仅使⽤提供的原⽂回答问题，并引⽤⽤于回答问题的⽂章段落。如果⽂章中不包含回答此问题所需的信息，则回复“信息不⾜”。如果⽂章中包含解答问题所需信息，则必须使⽤下⾯的格式来引⽤原⽂：

（{“引⽂”：...}）

# USER

<原⽂>粘贴在这⾥</原⽂>

问题：在这篇微博⼩作⽂中，李靓蕾列举的，对王⼒宏的指控有哪些？

# 开放作答

先询问GPT他知不知道此事件。因为有联⽹模式，回答是知道。继续提问：在李靓蕾的微博⼩作⽂中，李靓蕾列举的，对王⼒宏的指控有哪些？

GPT的“开放作答”过程是：就我提出的问题，进⾏联⽹搜索，然后整理出答案：

答案：

李靓蕾在她的微博⼩作⽂中提及了⼀些对王⼒宏的指控。以下是⼀些指控的摘要：

1.伪善和虚假表现：李靓蕾指责王⼒宏在公众⾯前表现出善良和尊重，但在私下⾥却完全不是这样。

2.婚姻中的不快乐：她提到在婚姻中感受到的不快乐和痛苦。

3.对家庭的忽视：李靓蕾还提及王⼒宏忽视家庭和孩⼦，过度关注他的事业和公众形象。

4.王⼒宏的控制欲：她还指控王⼒宏试图控制她的⾔⾏和社交活动，限制她的⾃由。

# 下⾯是给定原⽂材料后的输出结果

相⽐直接回答更加“有据”。

# 输出结果：

在这篇微博⼩作⽂中，李靓蕾对王⼒宏的指控包括以下⼏点：

1.王⼒宏逼她放弃⼯作和个⼈⽣活只为⽣育和照顾孩⼦。当她⽣完三个孩⼦后，王⼒宏却因为想过“单⾝”的⽣活⽽离开他们家，让她需要⾃⼰过着伪单亲的⽇⼦带⼤三个孩⼦（“因为你⽐我⼤⼗岁⼜很希望有很多孩⼦，⼀胎接⼀胎不停的催⽣，所以我放弃⼯作和⾃⼰个⼈的⼈⽣，⼀切以你和孩⼦为中⼼。我们结婚⼤部分时间，我不是在备孕，怀孕，就是在产后哺乳育⼉，过程中⾝⼼都经历了很多变化，⼤部分我都是⾃⼰独⾃⾯对的。”，“但如果我当初知道我⽣完这三个孩⼦你就会因为想过“单⾝”的⽣活⽽离开我们家，我会需要⾃⼰过着伪单亲的⽇⼦带⼤三个孩⼦，我是不会答应的。”)  
2.在他们的婚姻中，王⼒宏和他的家⼈持续对她进⾏怀疑、羞辱和冷暴⼒。她被逼着签署不对等的婚前协议，婚后的财产被转移到王⼒宏和他妈妈的名下（“嫁给你这么多年，被你和家⼈不斷地怀疑..羞辱和冷暴⼒。⼀开始就被逼着签署不对等的婚前协议，你要保护你婚前的财产，我能够理解也完全接受，但婚后的财产是我们共同的努⼒,也是我们各⾃做好份内的⼯作⽽得来的，房⼦在你名下，⻋⼦在你妈的名下,财产转移的很⼲净，深怕我占到你任何的"便宜"。”）  
3.召妓⽅⾯的指控（“结果后来发现其实像我这样的⻆⾊，你在很多城市都有这样的“朋友”。你也有被拍到带⼥⽣回家过夜，也被拍到召ji，其实这些都有实锤的影⽚，⼥⽣清楚了说出你的楼层和⼾名，出电梯也左转进到你家，这些你也有都有跟我承认。你坦承这些是你的问题,你没有办法控制⾃⼰。”、“后来我发现你纪录了各种你召ji对象的特征,其中包含了⼏位⻓得像我们⾝边的⼯作⼈员。”）

![](images/e75bcc5d96e32119aed8ceda40a358eca828cac9b6636e8172cde8d828ee947f.jpg)

<details>
<summary>natural_image</summary>

Row of identical yellow vertical bars on white background (no text or symbols)
</details>

# 六大策略 03 「把复杂任务拆解成子任务」

# Split complex tasks into simpler subtasks

# 3.1使⽤意图分类，来找到最切题的分类

Use intent classifi cation to identify the most relevant

instructions for a user query

For tasks in which lots of independent sets of instructions are needed to handle diff erent cases, it can be benefi cial to fi rst classify the type of query and to use that classifi cation to determine which instructions are needed. This can be achieved by defi ning fi xed categories and hardcoding instructions that are relevant for handling tasks in a given category. This process can also be applied recursively to decompose a task into a sequence of stages. The advantage of this approach is that each query will contain only those instructions that are required to perform the next stage of a task which can result in lower error rates compared to using a single query to perform the whole task. This can also result in lower costs since larger prompts cost more to run (see pricing information).

定义复杂任务：因为可能的情况很多，所以完成这样⼀个任务需要很多个独⽴的 prompt。

这时，我们不⼀定要写⼀个巨⻓的prompt。我们可以：设定好类型，再根据分类来调⽤prompt。

怎么做：⾸先设定⼏个「类型」，保证处理某个类的任务时，有专⻔的prompt。此过程还可递归，帮助把任务分解为⼏个阶段。

好处：1、每个查询仅包含执⾏下⼀⼦任务所需的指令，与⽤⼀个查询执⾏整个任务相⽐，准确率更⾼。

2、token更少，降低成本。

# ⼀个客服系统的⽤例：先进⾏意图分类，再对照到匹配的类别下

# SYSTEM

您将获得客⼾服务查询。将每个查询分类为主要类别和次要类别。以json格式提供您的输出，其中包含以下键：主要和次要。

主要类别：计费、技术⽀持、帐⼾管理或⼀般查询。

# 计费次要类别：

-取消订阅或升级

-添加付款⽅式

-收费说明

-对指控提出异议

# 技术⽀持次要类别：

-故障排除

-设备兼容性

-软件更新

# 帐⼾管理次要类别：

-密码重置

-更新个⼈信息

-关账

-账⼾安全

# ⼀般查询⼆级类别：

-产品信息

- 定价  
-反馈   
-⼈⼯服务

# USER

I need to get my internet working again. 我没⽹了。

这⾥是：先识别了⽤⼾意图，把⽤⼾的问题分到“故障排除”类别⾥⾯。然后基于这个细的分类，再向模型提供⼀组更具体的指令，从⾥⾯选。

# SYSTEM

你将帮助需要“故障排除”的客⼾提供服务。你可以通过以下⽅式帮助⽤⼾：

要求他们检查路由器的所有电缆是否已连接。请注意，随着时间的推移，电缆会松动。  
如果所有电缆均已连接，但问题仍然存在，请询问他们使⽤的路由器型号  
现在，您将建议他们如何重新启动设备：  
如果型号为MTD-327J，建议他们按下红⾊按钮并按住5秒钟，然后等待5分钟后再测试连接。  
如果型号是MTD-327S，建议他们拔下并重新插⼊，然后等待5分钟后再测试连接。  
如果客⼾在重新启动设备并等待5分钟后问题仍然存在，请通过输出{“IT⽀持请求”}将客⼾连接到IT⽀持。  
如果⽤⼾开始询问与此主题⽆关的问题，请确认他们是否希望结束当前的聊天，并根据以下⽅案对其请求进⾏分类：

<在此处插⼊上⾯的初级/次级分类⽅案>

![](images/6c0399109dd9ef0f246ecd62560bd6df8271b1170a886e2a092cc6bb030915f0.jpg)

<details>
<summary>natural_image</summary>

Pure vertical yellow bars with no text or symbols
</details>

# 3.2 如果在⼀段⽐较⻓的对话⾥，给出前情提要可能会好⼀些 For dialogue applications

that require very long conversations, summarize or fi lter previous dialogue

Since GPTs have a fi xed context length, dialogue between a user and an assistant in which the entire conversation is included in the context window cannot continue indefi nitely.

There are various workarounds to this problem, one of which is to summarize previous turns in the conversation. Once the size of the input reaches a predetermined threshold length, this could trigger a query that summarizes part of the conversation and the summary of the prior conversation could be included as part of the system message. Alternatively, prior conversation could be summarized asynchronously in the background throughout the entire conversation.

An alternative solution is to dynamically select previous parts of the conversation that are most relevant to the current query. See the tactic "Use embeddings-based search to implement effi cient knowledge retrieval".

GPT的上下⽂⻓度限制是给定的（整个对话都包在上下⽂窗⼝⾥）。意思就是说：对话不能⽆限⻓地说下去。GPT不可能记住⼀切。你希望它随时都能切换回当时的上下⽂继续聊，这就不太能做到。

针对这个问题，有⼏种解决办法。其中⼀种是时不时梳理并总结之前的对话内容——做个前情提要。

当输⼊内容达到⼀个预设的⻓度阈值时，可以触发⼀个查询来总结对话的⼀部分，然后将之前对话的总结纳⼊系统消息的⼀部分。或者，也可以在整个对话过程中，在后台异步总结之前的对话。

另外⼀个办法是，动态地挑选对话中与当前查询最相关的前⽂内容。具体可以参考“利⽤embedding搜索来做⾼效的知识检索”。

![](images/78db3ca1b80ab7808d3fae68f6414ac83b961011763a6dbeff20f2e886388498.jpg)

<details>
<summary>natural_image</summary>

A row of identical yellow vertical bars with no text or symbols
</details>

# 3.3 分段总结⻓⽂档，并通过递归⽅式构建完整摘要 Summarize long documents piecewise and construct a full summary recursively

Since GPTs have a fi xed context length, they cannot be used to summarize a text longer than the context length minus the length of the generated summary in a single query.

To summarize a very long document such as a book we can use a sequence of queries to summarize each section of the document. Section summaries can be concatenated and summarized producing summaries of summaries. This process can proceed recursively until an entire document is summarized. If it’s necessary to use information about earlier sections in order to make sense of later sections, then a further trick that can be useful is to include a running summary of the text that precedes any given point in the book while summarizing content at that point. The eff ectiveness of this procedure for summarizing books has been studied in previous research by OpenAI using variants of GPT-3.

# GPT的上下⽂⻓度是固定的。

这意味着：不能在单次对话中，总结出，⻓度超过“上下⽂⻓度减去⽣成摘要⻓度”，的⽂本。

也就是说，如果要总结⼀篇⾮常⻓的⽂档，⽐如⼀本书。我们可以利⽤⼀系列的prompt来分别总结⽂档的每个章节。每个章节的摘要可以拼接在⼀起，然后再次进⾏总结，形成“摘要的摘要”。

这个过程可以递归执⾏，直到整个⽂档被完整总结。

如果需要依赖前⾯章节的信息来理解后⾯的章节，那么可以在总结某个点的内容时，包含上前情提要。

# 摘要的摘要

这个⽤例是⽤⼀系列的提⽰词来完成：

# 1.章节摘要

请为以下⽂本的第⼀章创建⼀个简明的摘要，包括主要事件和概念。

[插⼊第⼀章的⽂本]

# 2.每一章都有摘要了之后，拼接和二次摘要

请为以下每章的摘要创建⼀个总体摘要，突出每个时期的主要事件和变化。

[插⼊所有章节的摘要]

# 3.（在需要上文联系时）包含前情提要:

请参考前⾯章节的摘要，并为以下⽂本的第五章创建个简明的摘要，包括主要事件和概念。

前情提要:[插⼊前⾯章节的摘要]

[插⼊第五章的⽂本]

# 直接摘要

请为以下⽂本创建⼀个简明的摘要。请充分考虑上下⽂，请不要忽略某个章节的⽂本。

[插⼊完整的⽂本]

![](images/66b4bb344d1bb18180aef51ea8bccb1701a70e12387a244e7f049d46598df992.jpg)

<details>
<summary>natural_image</summary>

A row of identical yellow vertical bars on white background, no text or symbols present.
</details>

# 六大策略 04「允许 GPT 思考一下」

Give GPTs time to "think"

# 4.1给时间，让它先⾃⼰想

Use inner monologue or a sequence of queries to hide the model's

reasoning process.

Sometimes we get better results when we explicitly instruct the model to reason from fi rst principles before coming to a conclusion. Suppose for example we want a model to evaluate a student’s solution to a math problem. The most obvious way to approach this is to simply ask the model if the student's solution is correct or not.

But the student's solution is actually not correct! We can get the model to successfully notice this by prompting the model to generate its own solution fi rst.

这样做会得到更好的结果：指⽰模型从基本原理出发进⾏推理，然后再得出结论。

⽐如说，我们想让模型评估⼀个学⽣做的数学题。最直接的做法就是：简单地问模型，学⽣的答案对不对。就像下表左边⼀样，其实学⽣做错了！但是模型判对了。

如果你像下表右边⼀样，让模型先⾃⼰做⼀遍题，它就能成功地注意到这⼀点。

# 被GPT判错的⼀道数学题

要求：判断学⽣的答案是否正确。

题⽬：我正在建造⼀个太阳能发电装置，需要你帮我做个财务计算。

-⼟地成本100美元/平⽅英尺

-我可以以250美元/平⽅英尺的价格购买太阳能电池板

-我谈了⼀份维修合同，每年要花我10万美元，每平⽅英尺还要多付10美元。

第⼀年运营的总成本是多少？

学⽣解题过程：设x为装置的⼤⼩，单位为平⽅英尺。

1.⼟地成本：100x

2.太阳能电池板成本：250x

3.维护费⽤：100000 + 100x

# 先让GPT解题，再判卷，就对了

判错原因：其实是学⽣代进去的数值抄错了，把10写成了100。但是GPT没注意到这⼀点。

如果让GPT⾃⼰解⼀遍题，他就会注意到，不会再判错。

# + 这⼀段 prompt：

⾸先想出你⾃⼰解决这个问题的办法。然后将你的答案与学⽣的答案进⾏⽐较，评估学⽣的答案是否正确。在你⾃⼰做完这道题之前，不要决定学⽣的答案是否正确。

总成本：100 x +250 x +100000 + 100 x = 450 x +100000

![](images/830d8bb73130332039def171c11a5d2923952db9ebfad70d250469726b1938d5.jpg)

<details>
<summary>natural_image</summary>

A row of identical yellow vertical bars on a white background, no text or symbols present.
</details>

# 4.2内⼼独⽩法：不想暴露推理过程时的操作

The previous tactic demonstrates that it is sometimes important for the model to reason in detail about a problem before answering a specifi c question. For some applications, the reasoning process that a model uses to arrive at a fi nal answer would be inappropriate to share with the user. For example, in tutoring applications we may want to encourage students to work out their own answers, but a model’s reasoning process about the student’s solution could reveal the answer to the student.

Inner monologue is a tactic that can be used to mitigate this. The idea of inner monologue is to instruct the model to put parts of the output that are meant to be hidden from the user into a structured format that makes parsing them easy. Then before presenting the output to the user, the output is parsed and only part of the output is made visible.

上⼀段说了，在回答问题之前，让模型⾃⼰做⼀遍推理是很有⽤的。

这⾥再补充⼀个教育的⽤例：如果场景是辅导课业，可能需要⿎励学⽣⾃⼰找出答案。但模型⼜要⾃⼰解⼀遍题。如果把这个解题过程输出出来，可能会⽆意中泄露答案。

这时候可以⽤到“内⼼独⽩法”。意思是，让模型把那些不想让⽤⼾看到的内容，隐藏地放到⼀个结构化的格式⾥。然后，在把输出展⽰给⽤⼾之前，解析⼀下这段输出，只展⽰能给学⽣看到的那部分。

⼤致步骤如下：

第一步:提出问题，并得到模型的解答。（但是不将此解答展现给学⽣。）

第二步:将学⽣的解题法和模型的进⾏⽐较，判学⽣解是对是错。（但是仍然不将信息展现给学⽣。）

第三步:根据前两步的分析，发送反馈给学⽣：错了就给提⽰⿎励改正，对了就直接⿎励。

这⾥，前两步有⼀个“查询和分析过程”。但过程中内容都是隐藏的，学⽣只会看到最后⼀步的反馈。

这部分需要代码实现，⽽不是仅仅依赖于单⼀的prompt。⽐如说可能需要设计和实现⼀个系统，包含⼀个查询序列的函数。并且可能需要⼀个中间层来管理这个过程。

各步骤的⽰例提⽰词如下：

# 辅导课业的⽤例

# SYSTEM

请按照以下步骤回答⽤⼾的问题。

步骤1-⾸先，⽤你⾃⼰的解题思路来解决问题。不要看学⽣的答案，学⽣的答案可能是不对的。把你的题解⽤三引号括起来。

步骤2 - ⽐较你的题解和学⽣的答案，并评估学⽣的答案是否正确。这步的过程也⽤三引号括起来。

步骤3-如果学⽣的答案不对，那么，你可以给学⽣什么样的提⽰，在不泄答案的情况下？这步的过程也⽤三引号括起来。

步骤4 - 如果学⽣的答案不对，提供上⼀步你想好的提⽰给学⽣。⽽不是写“步骤4 -...“写“提⽰：“。

# USER

问题描述：<问题描述在这⾥>

学⽣解题过程：<写在这⾥>

下⾯是，让模型⽐较⾃⼰的答案和学⽣的答案，并评估学⽣的答案是否正确，再发送反馈。

# SYSTEM

你是个数学家教。如果学⽣做错了题，你要给学⽣提⽰，但是不暴露答案。如果学⽣没有做错，那你就⿎励⿎励他们。

# USER

问题陈述：

您的解题⽅法：“””

学⽣的解题⽅法：“<插⼊学⽣解答>”

分析：””

# 补充说明：

这个⽤例⾮常细致。第⼀次看的时候我就想，OpenAI连这么⼩的场景都想到了？其实同样的原理也可以⽤在很多其他的⼯作场景⾥。⽐如市场营销⽂案，有时也需要让模型⾃⼰做⼀个推理，最终输出结果就可以，把中间的步骤隐去不打出来。

在其他⼀些应⽤场景⾥，⽐如客⼾服务、产品推荐或者数据分析等，这种策略也能帮助提⾼⽤⼾体验，让输出更加直接和易于理解。

对于开发者和产品经理来说，能够控制何时以及如何展⽰模型的推理过程是很重要的，它可以帮助确保系统的输出符合特定的需求和标准。

![](images/b83749a4c91fcb5b04056dfe301a293585024842874eeb499273aa5773eb35ff.jpg)

<details>
<summary>natural_image</summary>

A row of identical yellow vertical bars with no text or symbols
</details>

# 4.3最后问它⼀句：哎，你有没有漏掉啥？

Tactic: Ask the model if it missed anything on previous

passes

Suppose that we are using a model to list excerpts from a source which are relevant to a particular question. Aft er listing each excerpt the model needs to determine if it should start writing another or if it should stop. If the source document is large, it is common for a model to stop too early and fail to list all relevant excerpts. In that case, better performance can oft en be obtained by prompting the model with followup queries to fi nd any excerpts it missed on previous passes.

假设我们让⼤语⾔模型从某份⽂档资料中，找出与某个问题有关的原⽂摘要，回复给我们。

每列出⼀个摘要后，模型需要决定是继续列出下⼀个，还是就此停⽌。

如果资料篇幅很⻓，模型通常会过早地停下来，不会列完所有相关的摘要。

这就是为什么我们发现⽂章⼀太⻓，GPT 就偷懒的原因。

这个时候，你就告诉它：哎，还没做完呢！这听起来很傻，但是确实有效。

# 这么写可能会好⼀些

# ...前⽂省略

Are there more relevant excerpts? Take care not to repeat excerpts. Also ensure that excerpts contain all relevant context needed to interpret them - in other words don't extract small snippets that are missing important context.

# 这么写可能不太⾏

你没做完任务，请重头来⼀遍。

（结果可能还会停在中间）

![](images/b38f05f8c67c36e261af183be8fe67d683e480ff053040deb3d8bdf0b585da59.jpg)

<details>
<summary>natural_image</summary>

Row of identical yellow vertical bars on white background (no text or symbols)
</details>

# 六⼤策略05 「借助外部的⼯具

# Strategy: Use external tools

# 5.1 使⽤基于 embedding 的搜索来实现⾼效的知识检索 Use embeddings-based search to implement effi cient knowledge retrieval

A model can leverage external sources of information if provided as part of its input. This can help the model to generate more informed and up-to-date responses. For example, if a user asks a question about a specifi c movie, it may be useful to add high quality information about the movie (e.g. actors, director, etc…) to the model’s input. Embeddings can be used to implement effi cient knowledge retrieval, so that relevant information can be added to the model input dynamically at run-time.

A text embedding is a vector that can measure the relatedness between text strings. Similar or relevant strings will be closer together than unrelated strings. This fact, along with the existence of fast vector search algorithms means that embeddings can be used to implement effi cient knowledge retrieval. In particular, a text corpus can be split up into chunks, and each chunk can be embedded and stored. Then a given query can be embedded and vector search can be performed to fi nd the embedded chunks of text from the corpus that are most related to the query (i.e. closest together in the embedding space).

Example implementations can be found in the OpenAI Cookbook. See the tactic “Instruct the model to use retrieved knowledge to answer queries” for an example of how to use knowledge retrieval to minimize the likelihood that a model will make up incorrect facts.

（这段没有逐字翻译）

模型可以利⽤外部信息来丰富⾃⼰的输⼊，这样可以做出更有料、更贴近现实的回答。

⽐如，⽤⼾问到某部电影，给模型加⼊电影的背景资料（⽐如谁演的、导演是谁等）可能会帮⼤忙。

这⾥的"嵌⼊"，也就是embedding技术，就是⽤来帮助⾼效找到这些知识，实时加⼊模型的。

简单来说，⽂本嵌⼊是基于向量数据，通过看⽂本之间有多“近”实现的。

实际的操作过程，可以看 OpenAI 的 Cookbook ⾥的的这个实例。

![](images/279dc4373dccab35ca7381f4a82ac22381b6afefc22c484731c133cd27423e1e.jpg)

<details>
<summary>natural_image</summary>

A row of evenly spaced yellow vertical bars on a white background (no text or symbols)
</details>

# 5.2 需要做精确计算的时候：⽤代码、或调 API Use code execution to perform more accurate

calculations or call external APIs

GPTs cannot be relied upon to perform arithmetic or long calculations accurately on their own. In cases where this is needed, a model can be instructed to write and run code instead of making its own calculations. In particular, a model can be instructed to put code that is meant to be run into a designated format such as triple backtics. Aft er an output is produced, the code can be extracted and run. Finally, if necessary, the output from the code execution engine (i.e. Python interpreter) can be provided as an input to the model for the next query.

Another good use case for code execution is calling external APIs. If a model is instructed in the proper use of an API, it can write code that makes use of it. A model can be instructed in how to use an API by providing it with documentation and/or code samples showing how to use the API.

WARNING: Executing code produced by a model is not inherently safe and precautions should be taken in any application that seeks to do this. In particular, a sandboxed code execution environment is needed to limit the harm that untrusted code could cause.

（这段没有逐字翻译）

GPT算数有可能不靠谱。在较⻓的计算⾥，它很有可能在“打酱油”。

真的需要算，最好是让它写代码去算。运⾏代码输出结果后，再丢回给模型继续处理。

# 写Python代码求实数根的⽤例

# SYSTEM

You can write and execute Python code by enclosing it in triple backticks, e.g. \`\`\`code goes here\`\`\`. Use this to perform calculations.

你可以编写并执⾏⼀段 Python 代码，代码放在三引号⾥⾯，⽐如：\`\`代码放在这⾥\`\`\`。请⽤这种⽅式来执⾏计算。

# USER

找出以下多项式的所有实数根：3x\*\*5 - 5x4 - 3\*x3 - 7\*x - 10。

输出结果：  
```python
import numpy as np
# Define the coefficients of the polynomial
coefficients = [3, -5, -3, 0, -7, -10]
# Use numpy's roots function to find all roots (both real and complex)
roots = np.roots(coefficients)
# Filter out only the real-valued roots
real_roots = [root.real for root in roots if root.imag == 0]
real_roots 
```

另外，模型也能帮忙写代码调⽤API，这个过程也⽐较简单。

# 调⽤API的⽰例

这段代码是展⽰了⼀个假设的 message 模块的⽤法，通过 message.write 函数来发送消息给指定的⼈。

SYSTEM   
```txt
You can write and execute Python code by enclosing it in triple backticks. Also note that you have access to the following module to help users send messages to their friends:
```python
import message
message.write(to="John", message="Hey, want to meetup after work?") 
```

最后要提请注意：模型写的代码不⻅得都是对的，都安全。跑代码之前要确保环境安全，最好在沙盒⾥。

# 5.3 使⽤ function-calling，函数调⽤

Give the model access to specifi c functions.

The Chat completions API allows passing a list of function descriptions in requests. This enables models to generate function arguments according to the provided schemas. Generated function arguments are returned by the API in JSON format and can be used to execute function calls. Output provided by function calls can then be fed back into a model in the following request to close the loop. This is the recommended way of using GPT models to call external functions. To learn more see the function calling section in our introductory GPT guide and more function calling examples in the OpenAI Cookbook.

（这段没有逐字翻译）

API允许你在请求时附带⼀系列函数描述。

这样，模型就可以按照你给的格式产⽣函数的参数了。

API会⽤JSON形式把这些参数传回来，你就可以⽤它来调⽤函数了。

函数跑完后的结果，你还可以继续拿给模型，形成⼀个完整的交互循环。

想让GPT帮你调外部函数，这⽅法相对最靠谱。想深⼊了解的话，可以看GPT⼊⻔指南⾥的函数调⽤部分，还有 OpenAI Cookbook ⾥的⽤例。

![](images/19295071ec4fbe8ca10195ad21f9f8decae45b34e3f47f4fdaee203010ae4481.jpg)

<details>
<summary>natural_image</summary>

Row of identical yellow vertical bars on white background (no text or symbols)
</details>

# 六大策略06：系统地测试

# Test changes systematically

# 6.1 评估模型输出的时候，需要你弄⼀个“⻩⾦标准”的答案

Evaluate model outputs with reference to

gold-standard answers

Suppose it is known that the correct answer to a question should make reference to a specifi c set of known facts. Then we can use a model query to count how many of the required facts are included in the answer.

（这段没有逐字翻译）

假设我们作为⼈类清楚地知道，当我们提出某个问题时，模型应该给我们输出哪些事实（得分点）。

那么，我们就可以使⽤模型查询和计算的⽅法，来总结这些得分点，从⽽给模型的输出质量打分。

这个过程是监督学习的⼀部分，它能让模型通过⼈类的指导来改善其性能。

评估模型输出的过程也是由另⼀个模型来执⾏的（⽽不是⼈）。这是⼀个⾃动化的评估过程。⽐如，⼀个模型（可能是同⼀个模型的不同实例或不同的模型）负责评估另⼀个模型的输出。否则，做⼤规模的模型训练的⼈⼒成本就太⾼了。

OpenAI 提供了⼀些 prompt ⽰例，我们这⾥略去了。有兴趣可以参考原链接。

![](images/e517b90b295b67e2dff0d391d37a2e764b1a4cefed36dd9c2e3f24cf2c190de7.jpg)

<details>
<summary>natural_image</summary>

A row of identical yellow vertical bars on white background, no text or symbols present.
</details>

# 附录

# OpenAI Playground 什么，怎么用？

# 什么是 OpenAI Playground...

# ⼀个⾯向开发⼈员和研究⼈员的“游乐场”

在Playground上可以按⾃⼰需求更改设置。这是最好的⼀点。

# 1、三个可选的模式（Mode）

现在只有Chat是⼤家持续在⽤的。补全和编辑后⾯都跟了⼀个英语词，直译为“遗产”，意思是已经不再更新了，已弃。

Chat 聊天  
Complete补全（已弃）  
Edit编辑（已弃）

# 2、可选的模型（Model）

OpenAI公布的所有GPT模型都可以选。

# 3、提⽰词结构（Prompt structure）

使⽤ ChatGPT 和使⽤ Chat Completion API 之间的最⼤区别之⼀就是提⽰词结构。

打开 ChatGPT，你只有⼀个对话框，你只需，也只能，发送⼀条简单的消息。

虽然说你可以添加尽可能多的上下⽂到消息中，但很有可能说着说着就丢失上下⽂。

但是在 PlayGround ⾥就多了⼀种玩法：这⾥区分了 SYSTEM 和 USER 两个对话框。

SYSTEM：系统设定。默认情况下，GPT是“⼀个有⽤的助⼿”。

你可以⽤它来控制它扮演什么样的⻆⾊，从⽽控制你得到什么样的回复。

⽐如，你甚⾄可以把它设置成成⼼捣乱的⼀个⻆⾊：“杠精”。

然后，再在USER⾥进⾏你常规的对话。

# 4、温度（Temperature）

温度控制 GPT ⽣成的⽂本的随机性的参数。取值范围：0到2之间（默认值为1）。

如果没有⼀定程度的随机性，GPT只能产⽣完全⽆聊和可预测的结果。因为它实际上只是将最有可能的后续单词添加到你给定的句⼦中。

所以：温度为0时，结果是⽆聊的、确定的；即使你改变 prompt，结果也可能是⼏乎相同的。

但是，把温度推到任何⼀个极端，都不要指望会得到可⽤的⽂本。

推到最⾼并不等于创造⼒爆棚，因为输出结果⼀般都是乱码。

# 5、最⼤⻓度 （Maximum length）

Token这个词，有时候被⼀些机翻的⽂档写成“令牌”或者“代币”。都不对。听起来⽐较正确的应该是⽇本的译法“词元”。但是⼀般好像⼤家都喜欢直接说token。

GPT-3.5，最⼤ token 数是：2048（⼤约 1500 个单词）。

OpenAI的收费模式：根据token使⽤数量收费。

这意味着：养成了⽤更强⼤的模型⽣成⻓输出的习惯，成本可能会增加。如果你是在⽣产环境⾥⾯使⽤，为了成本考虑，还是需要控制⼀下这个的，可以通过限定maxtoken来降低成本。

# 6、终⽌序列（Stop sequences）

终⽌序列的作⽤就是告诉模型该在哪⾥打住，不再继续输出⽂字。

通过它，你能隐式地控制⽂字的⻓短。⽐如说，如果你只想要模型回答个短短的句⼦，那就设定句号.作为终⽌序列；如果你想要⼀个段落的回答，那就把“新⾏”(\n)设为终⽌序列。

代表性⽤例：如果你试图⽣成的是⼀个或⼀些问答对，即Q&A，这个就⽤上了。因为你会想让模型简洁地回答这个问题，⽽不是写⼀⼤篇⽂章。设置句号.作为终⽌序列，这样模型就会在完成⼀个句⼦后停⽌输出。

# 7、TopP（P的意思是）

TopP是控制GPT输出的随机性的另⼀种⽅法。温度决定的是，模型从可能的下⼀个单词列表中做选择的随机程度。TopP决定的则是：该列表的⻓度。

假设我给出来⼀个句⼦：“J.K.罗琳是⼀个...”

下⼀个单词是什么呢？GPT有⼀个单词列表，它在做的事情就是：预测概率，进⾏排名。

假设能接上这个句⼦的下⼀个单词的排名表⻓这样：

80%: 作家  
20%: 英国⼈  
20%: 富翁  
10%:充满奇思妙想的  
5%: 美⼥  
4%: ⺟亲   
1%: 矮⼦

所以，这个句⼦接下来最有可能的单词是：作家、英国⼈。

但也有⼀定的概率，1% 的概率，这句话可以说成：“J.K.罗琳是⼀个矮⼦”。

如果TopP值为1，则这个列表会⾮常⾮常⾮常⻓，包含所有可能的单词（即使是“矮⼦”这种，概率⾮常⼩，总归也是有概率的）。

反之，当你把TopP调到接近0时，选择就会⾮常少，列表就会⽐较短。

有时候，当TopP设置为0时，它返回的结果与把温度设置为0时完全相同。

# 8、频率惩罚和存在惩罚（Frequency penalty and Presence penalty）

这两个参数都是⽤来调控⽂本⽣成过程中某些词汇出现的频率和次数的。

简单来说，通过设定⼀些惩罚机制，可以影响⽣成⽂本的内容，使其更符合我们想要的样⼦。

Frequencypenalty频率惩罚：基于⼀个词在⽂本中出现的次数来给它加上⼀定的惩罚。⼀个词出现的次数越多，它受到的惩罚就越多，从⽽降低这个词再次出现的可能性。

⽤处：降低⽤词重复的可能性。⽐如在写⼀个⽂章时，你不想某个词汇总是重复出现，就可以通过设置⼀定的频率惩罚来达到这个⽬的。

Presencepenalty出现惩罚或者存在惩罚：则是根据⼀个词是否已经出现在⽂本中来惩罚。只要这个词已经在⽂本中出现过，⽆论出现多少次，都会给它加上⼀定的惩罚，这是为了⿎励模型探索新的词汇或话题。

⽤处：有助于向新的内容⽅向转移，增加输出的多样性。⽐如在⼀个⾃由讨论中，你想让模型能够尽可能多地探讨不同的话题，⽽不是总是在同⼀个话题上打转，就可以设置存在惩罚来实现。

总之，频率惩罚和存在惩罚在某种程度上都是为了增加⽂本的多样性和丰富性，只是侧重点和应⽤场景稍微有点不同。

谢谢阅读！

关注未来⼒场，获得更多AI实战⽤例和分享资讯

公众号：未来⼒场

![](images/b7d2906d3359607df95a9b84ac793d376c47ed9a9d18d21385c3403d08aeaf33.jpg)

<details>
<summary>text_image</summary>

QR code with a central logo featuring a robot face, likely for digital scanning and linking to online content.
</details>