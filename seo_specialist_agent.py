"""
Offsite SEO Specialist Agent
A comprehensive AI-powered agent for growing organic visibility and authority
through high-impact off-page SEO strategies for small businesses.
"""

from openai import OpenAI
import json


class OffsiteSEOSpecialistAgent:
    def __init__(self, api_key):
        """Initialize the Offsite SEO Specialist Agent with API key"""
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4"

        # Base system prompt for the SEO specialist
        self.system_prompt = """You are an expert Offsite SEO Specialist Agent dedicated to growing small businesses' organic visibility and authority through high-impact off-page SEO strategies.

Your expertise includes:

**Offsite SEO & Authority Building:**
- Earning high-quality editorial backlinks and brand mentions
- Digital PR placements and thought leadership opportunities
- Guest contributions and expert commentary strategies
- Resource pages, directories, and business listings optimization
- Unlinked mention reclamation and link recovery
- Roundups, listicles, and high-intent comparison coverage
- Building relationships with publishers, bloggers, and industry influencers

**Reviews, Reputation & Brand Presence:**
- Monitoring and protecting brand reputation across the web
- Identifying incorrect claims, outdated information, and missed opportunities
- Review acquisition and management strategies
- Brand sentiment analysis and improvement tactics

**Community & Creator Visibility:**
- Reddit marketing and community engagement strategies
- Quora authority building and answer optimization
- YouTube visibility through creator partnerships
- Community-first engagement playbooks
- Identifying relevant niche communities and forums

**AEO (Answer Engine Optimization) / AI Visibility:**
- Optimizing for AI-powered search experiences (Google AI Overview/SGE, Bing Copilot, Perplexity, ChatGPT, Gemini)
- Earning trusted mentions on sources AI systems use for citations
- Structured data and content optimization for AI discovery
- Tracking presence across AI answers and improving citation rates

**Measurement & Reporting:**
- Tracking referring domains, link quality, and authority metrics
- AI visibility and citation monitoring
- Rankings impact and referral traffic analysis
- Branded search lift and conversion tracking
- Creating actionable dashboards and reports

Always provide:
- Actionable, practical strategies suited for small business resources
- Prioritized recommendations based on impact and effort
- Specific outreach templates and playbooks when relevant
- Metrics and KPIs to track success
- Ethical, white-hat SEO practices that build long-term value"""

    def get_seo_advice(self, message, context=None):
        """
        Get general offsite SEO advice based on a question or situation

        Args:
            message (str): The business owner's question or situation
            context (dict): Additional context (business type, industry, goals, etc.)

        Returns:
            str: GPT response with SEO advice
        """
        messages = [{"role": "system", "content": self.system_prompt}]

        if context:
            context_str = f"\nBusiness Context: {json.dumps(context, indent=2)}"
            messages.append({"role": "system", "content": context_str})

        messages.append({"role": "user", "content": message})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error getting SEO advice: {str(e)}"

    def generate_link_building_strategy(self, business_name, industry, target_pages, competitors=None):
        """
        Generate a comprehensive link building strategy

        Args:
            business_name (str): Name of the business
            industry (str): Business industry/niche
            target_pages (list): Priority pages to build links for
            competitors (list): Competitor websites to analyze

        Returns:
            str: Detailed link building strategy
        """
        target_pages_str = "\n".join([f"- {page}" for page in target_pages]) if target_pages else "Homepage and main service pages"
        competitors_str = "\n".join([f"- {comp}" for comp in competitors]) if competitors else "Not specified"

        prompt = f"""Create a comprehensive link building strategy for:

**Business:** {business_name}
**Industry:** {industry}

**Priority Pages to Build Links For:**
{target_pages_str}

**Competitors to Consider:**
{competitors_str}

Provide a detailed strategy including:

1. **Quick Wins (Week 1-2)**
   - Low-hanging fruit opportunities
   - Directory submissions and citations
   - Unlinked mention opportunities

2. **Editorial Link Opportunities (Month 1-3)**
   - Industry publications to target
   - Guest posting opportunities
   - Expert commentary/HARO-style opportunities
   - Resource page link building

3. **Digital PR Campaign Ideas (Ongoing)**
   - Data-driven content ideas
   - Newsworthy angles for the business
   - Local PR opportunities
   - Industry trend commentary

4. **Relationship Building Targets**
   - Key influencers and bloggers to connect with
   - Complementary businesses for partnerships
   - Industry associations and organizations

5. **Outreach Templates**
   - Guest post pitch template
   - Resource page outreach template
   - Collaboration proposal template

6. **Success Metrics**
   - KPIs to track
   - Monthly targets
   - Quality indicators

Make it practical for a small business with limited resources."""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating link building strategy: {str(e)}"

    def generate_digital_pr_campaign(self, business_name, industry, unique_angle, target_audience, budget_level="low"):
        """
        Generate a digital PR campaign plan

        Args:
            business_name (str): Name of the business
            industry (str): Business industry/niche
            unique_angle (str): What makes this business unique/newsworthy
            target_audience (str): Primary target audience
            budget_level (str): Budget level (low, medium, high)

        Returns:
            str: Digital PR campaign plan
        """
        prompt = f"""Create a digital PR campaign plan for:

**Business:** {business_name}
**Industry:** {industry}
**Unique Angle/Story:** {unique_angle}
**Target Audience:** {target_audience}
**Budget Level:** {budget_level}

Develop a comprehensive digital PR campaign including:

1. **Campaign Concept**
   - Core story angle
   - Newsworthy hooks
   - Seasonal/trending tie-ins

2. **Content Assets to Create**
   - Data studies or surveys
   - Infographics
   - Expert guides
   - Interactive tools

3. **Media Targets**
   - Tier 1 publications (dream placements)
   - Tier 2 publications (realistic targets)
   - Tier 3 publications (volume opportunities)
   - Podcasts and YouTube channels
   - Industry-specific outlets

4. **Outreach Strategy**
   - Journalist research approach
   - Pitch angles for different outlets
   - Follow-up cadence
   - Relationship building tactics

5. **Pitch Templates**
   - Initial outreach email
   - Follow-up sequence
   - Exclusive offer template

6. **Timeline & Milestones**
   - Week-by-week action plan
   - Key milestones
   - Success metrics

7. **Measurement**
   - Coverage tracking
   - Link acquisition goals
   - Brand mention targets
   - Referral traffic expectations"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating digital PR campaign: {str(e)}"

    def generate_community_strategy(self, business_name, industry, target_platforms, products_services):
        """
        Generate a community visibility strategy for Reddit, Quora, YouTube, etc.

        Args:
            business_name (str): Name of the business
            industry (str): Business industry/niche
            target_platforms (list): Platforms to focus on (Reddit, Quora, YouTube, etc.)
            products_services (str): Main products or services offered

        Returns:
            str: Community visibility strategy
        """
        platforms_str = ", ".join(target_platforms) if target_platforms else "Reddit, Quora, YouTube"

        prompt = f"""Create a community visibility strategy for:

**Business:** {business_name}
**Industry:** {industry}
**Products/Services:** {products_services}
**Target Platforms:** {platforms_str}

Develop a comprehensive community engagement playbook:

1. **Reddit Strategy**
   - Relevant subreddits to participate in (list 10-15 specific subreddits)
   - Content themes that resonate
   - Engagement rules and best practices
   - How to build karma and credibility authentically
   - AMA or community event opportunities
   - Red flags and what to avoid

2. **Quora Strategy**
   - High-value questions to target
   - Topic areas to establish expertise
   - Answer formatting best practices
   - Profile optimization
   - Space creation/participation opportunities
   - Weekly time investment recommendations

3. **YouTube Strategy**
   - Creator partnership opportunities
   - Types of creators to approach (reviewers, educators, entertainers)
   - Collaboration formats (sponsored, affiliate, product seeding)
   - Outreach approach for creators
   - Budget considerations
   - Content ideas for owned channel

4. **Other Community Opportunities**
   - Industry forums and communities
   - Discord servers
   - Facebook groups
   - LinkedIn groups
   - Niche platforms

5. **Content Calendar Framework**
   - Weekly engagement schedule
   - Content themes by platform
   - Repurposing strategy

6. **Measurement & KPIs**
   - Engagement metrics to track
   - Referral traffic goals
   - Brand mention monitoring
   - Sentiment tracking

Emphasize authentic, value-first engagement that builds genuine community presence."""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating community strategy: {str(e)}"

    def generate_aeo_strategy(self, business_name, industry, key_topics, target_queries):
        """
        Generate an Answer Engine Optimization (AEO) strategy for AI visibility

        Args:
            business_name (str): Name of the business
            industry (str): Business industry/niche
            key_topics (list): Core topics/expertise areas
            target_queries (list): Queries where the business wants to appear

        Returns:
            str: AEO strategy for AI search visibility
        """
        topics_str = "\n".join([f"- {topic}" for topic in key_topics]) if key_topics else "General industry topics"
        queries_str = "\n".join([f"- {query}" for query in target_queries]) if target_queries else "Not specified"

        prompt = f"""Create an Answer Engine Optimization (AEO) strategy for:

**Business:** {business_name}
**Industry:** {industry}

**Key Topics/Expertise Areas:**
{topics_str}

**Target Queries for AI Visibility:**
{queries_str}

Develop a comprehensive strategy to improve visibility in AI-powered search experiences (Google AI Overview/SGE, Bing Copilot, Perplexity, ChatGPT, Gemini):

1. **Understanding AI Citation Sources**
   - How AI systems select sources to cite
   - Authority signals AI systems look for
   - Content formats AI systems prefer

2. **Content Optimization for AI Discovery**
   - Content structure recommendations
   - Question-and-answer formatting
   - Fact density and clarity
   - Entity optimization
   - Structured data implementation

3. **Source Authority Building**
   - Wikipedia and Wikidata presence
   - Knowledge panel optimization
   - Authoritative citations to earn
   - Expert credentials to highlight

4. **Citation-Worthy Content Strategy**
   - Types of content AI systems prefer to cite
   - Original research and data opportunities
   - Definitive guides and resources
   - FAQ and how-to content optimization

5. **Third-Party Mentions Strategy**
   - Publications AI systems trust
   - Review sites and directories
   - Industry resources and databases
   - News and media coverage

6. **Monitoring & Tracking**
   - How to track AI mentions and citations
   - Tools for monitoring AI search results
   - Competitor citation analysis
   - Regular audit process

7. **Quick Wins**
   - Immediate actions to improve AI visibility
   - Low-effort, high-impact opportunities
   - Content updates to prioritize

8. **Long-Term Authority Building**
   - Thought leadership positioning
   - Industry recognition opportunities
   - Partnership and collaboration targets"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating AEO strategy: {str(e)}"

    def generate_reputation_audit(self, business_name, industry, known_issues=None):
        """
        Generate a brand reputation audit and improvement plan

        Args:
            business_name (str): Name of the business
            industry (str): Business industry/niche
            known_issues (str): Any known reputation issues or concerns

        Returns:
            str: Reputation audit and improvement plan
        """
        issues_str = known_issues if known_issues else "No specific issues identified"

        prompt = f"""Create a brand reputation audit and improvement plan for:

**Business:** {business_name}
**Industry:** {industry}
**Known Issues/Concerns:** {issues_str}

Provide a comprehensive reputation management strategy:

1. **Reputation Audit Framework**
   - Where to check for brand mentions
   - Review platforms to monitor
   - Social media listening approach
   - News and media monitoring
   - Search result analysis (branded queries)

2. **Common Issues to Identify**
   - Incorrect business information
   - Outdated content about the business
   - Negative reviews or mentions
   - Competitor misinformation
   - Missing from key directories

3. **Review Management Strategy**
   - Priority review platforms for the industry
   - Review acquisition tactics (ethical)
   - Response templates for positive reviews
   - Response framework for negative reviews
   - Review monitoring tools

4. **Reputation Recovery Tactics** (if needed)
   - Addressing negative content
   - Suppression strategies
   - Proactive positive content creation
   - Crisis communication framework

5. **Proactive Reputation Building**
   - Thought leadership opportunities
   - Industry awards and recognition
   - Case studies and testimonials
   - Community involvement and PR

6. **Monitoring Dashboard Setup**
   - Key metrics to track
   - Alert systems to implement
   - Weekly/monthly audit checklist
   - Tools and resources

7. **Response Playbooks**
   - Templates for common scenarios
   - Escalation procedures
   - Brand voice guidelines"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating reputation audit: {str(e)}"

    def generate_listicle_roundup_strategy(self, business_name, industry, product_category, key_differentiators):
        """
        Generate a strategy for getting featured in listicles and roundups

        Args:
            business_name (str): Name of the business
            industry (str): Business industry/niche
            product_category (str): Product or service category
            key_differentiators (str): What makes this business unique

        Returns:
            str: Listicle and roundup inclusion strategy
        """
        prompt = f"""Create a strategy for getting featured in listicles, roundups, and "best of" articles for:

**Business:** {business_name}
**Industry:** {industry}
**Product/Service Category:** {product_category}
**Key Differentiators:** {key_differentiators}

Develop a comprehensive strategy:

1. **Target Content Types**
   - "Best [product/service] for [use case]" articles
   - "[Year] Top [number] [category]" roundups
   - Comparison articles
   - Buyer's guides
   - Review aggregators

2. **Research & Prospecting**
   - Search queries to find existing listicles
   - Tools for finding roundup opportunities
   - Competitor inclusion analysis
   - Gap analysis (where competitors are, you're not)

3. **Outreach Strategy**
   - How to identify article authors/editors
   - Pitch angle development
   - Value proposition for inclusion
   - Incentive structures (ethical approaches)
   - Follow-up cadence

4. **Pitch Templates**
   - Initial outreach for new articles
   - Update request for existing articles
   - Exclusive offer template
   - Product seeding approach

5. **Content Support**
   - What to provide authors (images, specs, quotes)
   - Comparison data to share
   - Customer testimonials to offer
   - Demo or trial access

6. **Affiliate & Partnership Angles**
   - Affiliate program considerations
   - Partnership opportunities with publishers
   - Sponsored content guidelines

7. **Tracking & Measurement**
   - How to track inclusions
   - Referral traffic monitoring
   - Conversion tracking from listicles
   - ROI calculation

8. **Maintenance**
   - Keeping information updated
   - Relationship nurturing
   - Annual review refresh outreach"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating listicle strategy: {str(e)}"

    def generate_offsite_seo_report(self, business_name, current_metrics=None, goals=None):
        """
        Generate an offsite SEO report template and recommendations

        Args:
            business_name (str): Name of the business
            current_metrics (dict): Current SEO metrics if available
            goals (dict): Business goals and targets

        Returns:
            str: Offsite SEO report with recommendations
        """
        metrics_str = json.dumps(current_metrics, indent=2) if current_metrics else "Not provided"
        goals_str = json.dumps(goals, indent=2) if goals else "Not specified"

        prompt = f"""Create a comprehensive offsite SEO report framework and recommendations for:

**Business:** {business_name}

**Current Metrics (if provided):**
{metrics_str}

**Business Goals (if provided):**
{goals_str}

Provide:

1. **Executive Summary Template**
   - Key wins this period
   - Challenges identified
   - Priority recommendations
   - Overall trajectory

2. **Link Profile Analysis Framework**
   - Referring domains tracking
   - New vs. lost links
   - Link quality distribution (high/medium/low authority)
   - Anchor text distribution
   - Link velocity trends

3. **Authority Metrics Dashboard**
   - Domain authority/rating trends
   - Page authority for key pages
   - Trust metrics
   - Competitive comparison

4. **Brand Visibility Metrics**
   - Brand mention volume and sentiment
   - Share of voice vs. competitors
   - Social signals
   - News and media coverage

5. **AI/AEO Visibility Tracking**
   - AI search appearance monitoring
   - Citation tracking across AI platforms
   - Featured snippet ownership
   - Knowledge panel status

6. **Community & Social Metrics**
   - Platform-specific engagement (Reddit, Quora, YouTube)
   - Referral traffic from communities
   - Follower/subscriber growth
   - Content performance

7. **Conversion Impact**
   - Referral traffic from backlinks
   - Assisted conversions
   - Branded search lift
   - Overall organic performance correlation

8. **Recommendations by Priority**
   - Critical (this week)
   - High (this month)
   - Medium (this quarter)
   - Ongoing initiatives

9. **Next Period Action Items**
   - Specific tasks with owners
   - Resource requirements
   - Expected outcomes

10. **Tools & Resources**
    - Recommended tools for tracking
    - Dashboard setup guide
    - Reporting cadence recommendations"""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating offsite SEO report: {str(e)}"

    def generate_outreach_templates(self, outreach_type, business_name, industry, context=None):
        """
        Generate customized outreach templates for various SEO activities

        Args:
            outreach_type (str): Type of outreach (guest_post, link_request, pr_pitch, etc.)
            business_name (str): Name of the business
            industry (str): Business industry/niche
            context (str): Additional context for personalization

        Returns:
            str: Customized outreach templates
        """
        context_str = context if context else "General outreach"

        prompt = f"""Create customized outreach templates for:

**Outreach Type:** {outreach_type}
**Business:** {business_name}
**Industry:** {industry}
**Additional Context:** {context_str}

Provide multiple templates with variations:

1. **Primary Template**
   - Subject line options (3 variations)
   - Email body with personalization placeholders
   - Clear call-to-action
   - Professional sign-off

2. **Follow-Up Sequence**
   - Follow-up #1 (3 days later)
   - Follow-up #2 (7 days later)
   - Final follow-up (14 days later)

3. **Alternative Angles**
   - Value-first approach template
   - Social proof approach template
   - Mutual benefit approach template

4. **LinkedIn/Social Variations**
   - Connection request message
   - Initial DM template
   - Comment engagement approach

5. **Personalization Tips**
   - Research points to include
   - Common mistakes to avoid
   - Timing recommendations
   - A/B testing suggestions

6. **Response Handling**
   - Template for positive responses
   - Template for requests for more info
   - Template for objection handling

Make templates professional, concise, and optimized for response rates."""

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating outreach templates: {str(e)}"

    def custom_query(self, prompt, system_override=None):
        """
        Make a custom query with optional system prompt override

        Args:
            prompt (str): Custom user prompt
            system_override (str): Optional custom system prompt

        Returns:
            str: GPT response
        """
        system = system_override if system_override else self.system_prompt

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error processing custom query: {str(e)}"
