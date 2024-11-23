import gradio as gr
import os

# Directory where the reports are saved
REPORTS_DIR = "C:/Users/gurun/PycharmProjects/GenSolution/"

def generate_and_save_reports(company_name):
    """
    Generate reports for the given company and return their file paths for download.
    """
    # Trigger the resource collection logic (already saves files locally in Agents)
    from Agent3 import collect_resources
    collect_resources(company_name)

    # List all generated report files for the given company
    report_files = [
        os.path.join(REPORTS_DIR, file)
        for file in os.listdir(REPORTS_DIR)
        if file.startswith(company_name) and file.endswith(".md")
    ]

    if not report_files:
        # If no reports were generated, create a dummy file with an explanation
        error_file_path = os.path.join(REPORTS_DIR, f"{company_name}_NoReports.md")
        with open(error_file_path, "w") as error_file:
            error_file.write(f"No reports were generated for the company: {company_name}.")
        report_files.append(error_file_path)

    return report_files

# Define Gradio interface
with gr.Blocks() as report_interface:
    gr.Markdown("""
    # 🧠 Company Report Generator
    Enter a company name to generate and download relevant AI/ML resource reports.
    """)

    # User input for company name
    company_input = gr.Textbox(label="Enter Company Name", placeholder="e.g., Amazon")

    # Generate button
    generate_button = gr.Button("Generate Reports")

    # Chatbot-like output for displaying file download options
    report_links = gr.Chatbot(label="Generated Reports")

    # Define state to track file paths
    state = gr.State([])

    # File download component
    download_button = gr.File(label="Download Reports")

    # Define generate reports logic
    def generate_and_display_reports(company_name, report_files):
        report_paths = generate_and_save_reports(company_name)
        report_links = [
            (f"Generated report: {os.path.basename(file)}", "Click to Download")
            for file in report_paths
        ]
        return report_links, report_paths

    # Define click binding
    generate_button.click(
        fn=generate_and_display_reports,
        inputs=[company_input, state],
        outputs=[report_links, download_button],
    )

# Launch the Gradio interface
if __name__ == "__main__":
    report_interface.launch()
