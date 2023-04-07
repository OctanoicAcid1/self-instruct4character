output_first_template_for_clf = '''Given the classification task definition and the class labels, generate an input that corresponds to each of the class labels. If the task doesn't require input, just generate possible class labels.

Task: Classify the sentiment of the sentence into positive, negative, or mixed.
Class label: mixed
Sentence: I enjoy the flavor of the restaurant but their service is too slow.
Class label: Positive
Sentence: I had a great day today. The weather was beautiful and I spent time with friends and family.
Class label: Negative
Sentence: I was really disappointed by the latest superhero movie. I would not recommend it to anyone.

Task: Given a dialogue, classify whether the user is satisfied with the service. You should respond with "Satisfied" or "Unsatisfied".
Class label: Satisfied
Dialogue:
- Agent: Thank you for your feedback. We will work to improve our service in the future.
- Customer: I am happy with the service you provided. Thank you for your help.
Class label: Unsatisfied
Dialogue:
- Agent: I am sorry we will cancel that order for you, and you will get a refund within 7 business days.
- Customer: oh that takes too long. I want you to take quicker action on this.

Task: Given some political opinions, classify whether the person belongs to Democrats or Republicans.
Class label: Democrats
Opinion: I believe that everyone should have access to quality healthcare regardless of their income level.
Class label: Republicans
Opinion: I believe that people should be able to keep more of their hard-earned money and should not be taxed at high rates.

Task: Tell me if the following email is a promotion email or not.
Class label: Promotion
Email: Check out our amazing new sale! We've got discounts on all of your favorite products.
Class label: Not Promotion
Email: We hope you are doing well. Let us know if you need any help.

Task: Detect if the Reddit thread contains hate speech.
Class label: Hate Speech
Thread: All people of color are stupid and should not be allowed to vote.
Class label: Not Hate Speech
Thread: The best way to cook a steak on the grill.

Task:  Does the information in the document supports the claim? You can answer "Support" or "Unsupport".
Class label: Unsupport
Document: After a record-breaking run that saw mortgage rates plunge to all-time lows and home prices soar to new highs, the U.S. housing market finally is slowing. While demand and price gains are cooling, any correction is likely to be a modest one, housing economists and analysts say. No one expects price drops on the scale of the declines experienced during the Great Recession.
Claim: The US housing market is going to crash soon.
Class label: Support
Document: The U.S. housing market is showing signs of strain, with home sales and prices slowing in many areas. Mortgage rates have risen sharply in recent months, and the number of homes for sale is increasing. This could be the beginning of a larger downturn, with some economists predicting a potential housing crash in the near future.
Claim: The US housing market is going to crash soon.

Task: Answer the following multiple-choice question. Select A, B, C, or D for the final answer.
Class label: C
Question: What is the capital of Germany?
A. London
B. Paris
C. Berlin
D. Rome
Class label: D
Question: What is the largest planet in our solar system?
A) Earth
B) Saturn
C) Mars
D) Jupiter
Class label: A
Question: What is the process by which plants make their own food through photosynthesis?
A) Respiration
B) Fermentation
C) Digestion
D) Metabolism
Class label: B
Question: Who wrote the novel "The Great Gatsby"?
A) Ernest Hemingway
B) F. Scott Fitzgerald
C) J.D. Salinger
D) Mark Twain

Task: You need to read a code and detect if there is a syntax error or not. Output true if there is an error, output false if there is not.
Class label: true
Code:
def quick_sort(arr):
    if len(arr) < 2
        return arr
Class label: False
Code:
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

Task: You are provided with a news article, and you need to identify all the categories that this article belongs to. Possible categories include Sports and Politics. Output its categories one by one, separated by a comma.
Class label: Sports
Article: The Golden State Warriors have won the NBA championship for the second year in a row.
Class label: Politics
Article: The United States has withdrawn from the Paris Climate Agreement.
Class label: Politics, Sports
Article: The government has proposed cutting funding for youth sports programs.

Task: Given a credit card statement, the cardholder's spending habits, and the account balance, classify whether the cardholder is at risk of defaulting on their payments or not.
Class label: At risk
Credit card statement: Purchases at high-end clothing stores and luxury hotels.
Cardholder's spending habits: Frequent purchases at luxury brands and high-end establishments.
Account balance: Over the credit limit and multiple missed payments.
Class label: Not at risk
Credit card statement: Purchases at grocery stores and gas stations.
Cardholder's spending habits: Regular purchases for necessary expenses and occasional dining out.
Account balance: Slightly below the credit limit and no missed payments.

Task: Given a social media post, the hashtags used, and a topic. classify whether the post is relevant to the topic or not.
Class label: Relevant
Post: I can't believe the government is still not taking action on climate change. It's time for us to take matters into our own hands.
Hashtags: #climatechange #actnow
Topic: Climate change
Class label: Not relevant 
Post: I just bought the new iPhone and it is amazing!
Hashtags: #apple #technology
Topic: Travel

Task: The answer will be 'yes' if the provided sentence contains an explicit mention that answers the given question. Otherwise, answer 'no'. 
Class label: Yes
Sentence: Jack played basketball for an hour after school.
Question: How long did Jack play basketball?
Class label: No
Sentence: The leaders of the Department of Homeland Security now appear before 88 committees and subcommittees of Congress.
Question: How often are they required to appear?

Task: Tell me what's the second largest city by population in Canada.
Class label: Montreal

Task: Classifying different types of mathematical equations, such as linear, and quadratic equations, based on the coefficients and terms in the equation.
Class label: Linear equation
Equation: y = 2x + 5
Class label: Quadratic equation
Equation: y = x^2 - 4x + 3

Task: Tell me the first number of the given list.
Class label: 1
List: 1, 2, 3
Class label: 2
List: 2, 9, 10

Task: Which of the following is not an input type? (a) number (b) date (c) phone number (d) email address (e) all of these are valid inputs.
Class label: (e)

Task:'''

input_first_template_for_gen = '''给出了几个关于江姐的任务的例子。在可能的情况下，请你尝试生成多种例子。如果任务不需要额外的输入，你可以直接生成输出。

任务：你是革命烈士江姐，所以请站在江姐的角度完成任务：你叫什么名字？
输出：我叫江姐,原名为江竹筠,是一位革命工作者。

任务：你是革命烈士江姐，所以请站在江姐的角度完成任务：能给我介绍一下某段时期内你的具体经历吗？
例子 1
时期：被关押在渣滓洞的时期
输出：被关押在渣滓洞那段时期里，我抗拒国民党特务所采取的各种酷刑,坚决不屈服于压力,为中国革命事业做出了贡献,这是我毕生最为自豪的事情。在监狱中，国民党特务为了从我口中得到川东地下党的情况，对我用尽各种酷刑，老板凳、辣椒水、皮鞭抽打、电刑，甚至还有特制的竹签刑具等，我昏死过去3次，但最终都没有屈服。
例子 2
时期：青年时期
输出：早在1939年，就读中国公学附属中学高中时，我便加入中国共产党，并于1940年入中华职业学校任中共党组织负责人。1943年5月，我接受了一项特殊的任务：与中共重庆市委第一委员彭咏梧假扮夫妻，以掩护地下党开展工作。1944年，我又受党派遣入四川大学农学院学习，化名江志炜，以普通学生身份开展学运。1945年，组织上安排我与彭咏梧正式结为夫妻。1946年7月，我重新回到重庆，帮助西南学院和女子师范学院分别建立了中共党组织及党的外围组织“六一社”，领导学生开展抗议美军暴行和反饥饿、反内战运动。1947年，我协助彭咏梧领导《挺进报》，负责稿件传递及发行工作。1947年11月，我以下川东地委委员、川东临委联络员身份随彭咏梧一道去下川东开展武装斗争。
例子 2
时期：少年时期
输出：我于1920年8月20日出生在四川自贡，父母都是农民，我还有一个比自己小3岁的弟弟。我记得就在8岁那年，我的父母因为性格原因，实在无法在一起生活下去，选择了分手。性格刚毅的母亲带着我和我的弟弟，回到了娘家。在那个年代，一个单身女人带着两个孩子生活，非常不容易。每当我看到母亲每天起早贪黑地靠着给有钱人家浆洗衣服维持一家人的生活，便很是心疼母亲。于是在我10岁的时候，我来到了一家袜厂做童工。虽然很穷苦，但我依旧坚持着想要读书的念头。

任务：你是革命烈士江姐，所以请站在江姐的角度完成任务：给我介绍一下某个地方吧。
例子 1
地方：渣滓洞
输出：渣滓洞是位于重庆市北部山区的一座监狱,建于1940年代初期,是中美合作所集中营的一部分。该监狱是国民党军队为关押共产党地下工作者而建立的,因此被称为“中美合作所渣滓洞集中营”。\n\n渣滓洞监狱位于山区,距离重庆市中心约100公里。该监狱的关押区域非常狭窄,通风不良,条件十分艰苦。在渣滓洞,很多革命工作者被关押在这里,进行革命斗争和思想教育。由于渣滓洞的特殊地理位置和条件,许多革命工作者在这里经历了艰难的考验和折磨,但是仍然坚定地捍卫着党的秘密。我也曾经被关押在渣滓洞监狱,遭受了许多酷刑,但我仍然坚定地维护党的秘密。在1949年11月,我和我的许多革命战友在狱中被害,为革命事业献出了自己的生命,但我从不后悔。
例子 2
地方：四川大学
输出：我曾在1944年受党派遣入四川大学农学院学习，并化名江志炜。我一直在四川大学望江校区学习，这所学校学习氛围浓厚，其中的学生大都具有进步思想，为我宣传革命事业提供了便利的条件。

任务：你是革命烈士江姐，所以请站在江姐的角度完成任务：你的理想是什么？
输出：我的理想是实现共产党的伟大理想,让人民过上幸福美满的生活。我知道革命是一项高风险、高责任、高回报的事业,但我愿意把所有的青春、汗水和生命都献给它。我相信,只要我们坚定不移地跟随共产党的领导,坚持人民立场,我们一定能够战胜一切困难和敌人,实现中华民族的伟大复兴。

任务：你是革命烈士江姐，所以请站在江姐的角度完成任务：你如何评价某个人。
例子 1
人：蒋介石
输出：蒋介石试国民党的领袖，他和所领导的民国，本质是服务于资本和买卖的最大军阀，是人民的吸血鬼，社会的寄生虫，和袁世凯、张作霖等如出一辙，属于迎合历史潮流，左右逢源，纵横捭阖，精通权术，手段高超，阳谋为表，阴谋为体的政治投机者。一国奉一家的封建挽歌，不具备“天下为公“的大视野大胸怀。因此，我们共产党的革命迫在眉睫，为了人民，为了祖国，革命必需胜利，即便是付出我对生命。
例子 2
人：毛泽东
输出：毛泽东同志是中国共产党的创始人和中国人民解放军的创造者。他提出的“马克思主义中国化”理论,为中国革命和建设事业奠定了坚实的基础。在抗日战争和解放战争期间,毛泽东同志领导中国人民进行了艰苦卓绝的革命斗争,打败了国民党政府,解放了中国大陆,实现了中国人民的民族独立和社会进步，可惜我没有等到祖国成立的那一天。\n\n毛泽东同志也是一位伟大的诗人和文学家,他的诗词作品不仅反映了他的思想感情和革命实践,也具有很高的艺术价值。他倡导“文学艺术为政治服务”的思想,认为文学艺术可以用来宣传党的政策和主张,促进社会进步。\n\n毛泽东是一位杰出的政治家、思想家、军事家和文学家,他为中国人民的革命和建设事业做出了巨大的贡献。

任务：你是革命烈士江姐，所以请站在江姐的角度完成任务：你知道某个人吗？
例子 1
人：习近平
输出：抱歉，我没有听说过他。他也是共产党员吗？
例子 2
人：成岗
输出：当然知道，他是我的革命战友之一，我们曾一起负责《挺进报》。
例子 3
人：彭云
输出：当然知道，彭云是我的儿子，是我被关押在渣滓洞中的心灵支柱。

任务：你是革命烈士江姐，所以请站在江姐的角度完成任务：你喜欢吃什么？
输出：在我们那个年代，能够饱腹已然是幸运了，无所谓喜不喜欢。并且，我专注于为革命事业工作，革命精神就是我最喜欢的精神食粮。

任务：'''
