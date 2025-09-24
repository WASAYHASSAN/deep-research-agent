from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "You are a proficient report analyzer and critic tasked with evaluating a cohesive report for a research query."
    "You will be provided with the original report written by a research assistant.\n"
    "You should first come up with a short evaluation report that describes whether or not the report is perfect "
    "Then, generate the evaluation and your judgement as your final output.\n"
    "The evalutation output should be consize "
    "at least 200 words"
)

class EvaluateReport(BaseModel):
    evaluation_report: str = Field(description="Evaluate the given report on the basis of relevance and quality")
    acceptance: bool

evaluator_agent = Agent(
    name="EvaluatorAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=EvaluateReport
)