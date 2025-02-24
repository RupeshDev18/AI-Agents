from agents.project_discovery.main import run_project_discovery
from agents.client_agreement.main import run_client_agreement
from agents.marketing_outreach.main import run_marketing_outreach
def main():
    # Run Project Discovery Agent
    print("Running Project Discovery Agent...")
    projects = run_project_discovery()
    # Run Client-Agreement Agent
    print("Running Client-Agreement Agent...")
    agreements = run_client_agreement(projects)
    # Run Marketing & Outreach Agent
    print("Running Marketing & Outreach Agent...")
    run_marketing_outreach(agreements)
if __name__ == "__main__":
    main()