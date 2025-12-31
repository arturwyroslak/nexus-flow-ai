import os
import git
import tempfile
from pathlib import Path

class ContextPacker:
    """
    A simplified 'Repomix' implementation to pack repository contexts
    into LLM-friendly formats (XML/JSON).
    """
    
    def __init__(self, repo_url=None, local_path=None):
        self.repo_url = repo_url
        self.local_path = local_path
        self.temp_dir = None

    def _clone_repo(self):
        """Clones a remote repo to a temporary directory."""
        if self.repo_url:
            self.temp_dir = tempfile.mkdtemp()
            try:
                git.Repo.clone_from(self.repo_url, self.temp_dir)
                return self.temp_dir
            except Exception as e:
                return f"Error cloning repo: {str(e)}"
        return self.local_path

    def pack(self, format="xml"):
        """
        Packs the codebase into a single string.
        """
        target_dir = self._clone_repo()
        if not target_dir or (isinstance(target_dir, str) and target_dir.startswith("Error")):
            return target_dir

        packed_content = []
        
        if format == "xml":
            packed_content.append("<repository>")
        
        for root, _, files in os.walk(target_dir):
            if ".git" in root:
                continue
                
            for file in files:
                if file.startswith("."):
                    continue
                    
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, target_dir)
                
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        
                    if format == "xml":
                        packed_content.append(f'<file path="{rel_path}">\n<![CDATA[\n{content}\n]]>\n</file>')
                    else:
                        packed_content.append(f"--- FILE: {rel_path} ---\n{content}\n")
                except Exception:
                    continue # Skip unreadable files

        if format == "xml":
            packed_content.append("</repository>")
            
        return "\n".join(packed_content)

    def cleanup(self):
        """Cleans up temporary directories."""
        if self.temp_dir:
            import shutil
            shutil.rmtree(self.temp_dir)
