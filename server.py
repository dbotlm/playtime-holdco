#!/usr/bin/env python3
"""
Play Time VC - Full REST API & Static Server
Provides complete CRUD APIs for every single element on the website + persistent JSON storage.
"""

import os
import sys
import json
import mimetypes
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8888
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

# 100% Play Time VC Initial Default Dataset
DEFAULT_DATA = {
    "meta": {
        "title": "Play Time HoldCo",
        "description": "Sports-Technology Holding and Investment Company in San Francisco, backed By Lionel Messi & Razmig Hovaghimian",
        "favicon": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/6346b39e9440e56366adb435_Fav%20icon%20(1).png",
        "appleTouchIcon": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/6346e586f6f4a49ead3c317e_Icon.png"
    },
    "hero": {
        "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/6346a74e759e2a8a337b0dd5_Playtime.svg",
        "titlePart1": "At the intersection",
        "titlePart2": "of Sports & Technology"
    },
    "portfolio": [
        {
            "id": "field-ai",
            "name": "FieldAI",
            "tagline": "Autonomous brains for field robots",
            "url": "https://fieldai.com/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/67a22b735f490991a0746696_field%20ai.png",
            "bgClass": "full-6",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/69fd2d0ac1b5a18253587472_image-(7).avif",
            "logoContainerClass": "size",
            "imageClass": "image size",
            "isSizeM": False
        },
        {
            "id": "fish-audio",
            "name": "Fish Audio",
            "tagline": "Realistic AI Voice Maker",
            "url": "https://fish.audio/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/69f43c72c0b1a8ac332847fd_fish-clearspace.svg",
            "bgClass": "full-8-copy _9",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/69f6162a76aa5f9511c992c1_46b1ef2ded63ba4ec4ebb7c041a925a8_image-(5).avif",
            "logoContainerClass": "size_m",
            "imageClass": "image sie_big",
            "isSizeM": False
        },
        {
            "id": "world-labs",
            "name": "World Labs",
            "tagline": "Spatial AI for 3D environments",
            "url": "https://www.worldlabs.ai/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/69cc01d7564904aa43c16d70_Frame%20(1).svg",
            "bgClass": "full-8",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/69ccb24129c20307aa95de16_world.avif",
            "logoContainerClass": "size_m",
            "imageClass": "image sie_big",
            "isSizeM": False
        },
        {
            "id": "perceptron",
            "name": "Perceptron",
            "tagline": "Foundation models for the physical world",
            "url": "https://perceptron.inc/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/678f8fc7106e9d8021096404_image__3_-removebg-previeww%201.svg",
            "bgClass": "full-7",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/678f8c4cdd6b15715a48f4b5_image%20(2).avif",
            "logoContainerClass": "size",
            "imageClass": "image size",
            "isSizeM": False
        },
        {
            "id": "intangible",
            "name": "Intangible",
            "tagline": "3D visualization tool for creative teams",
            "url": "https://www.intangible.ai/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/69ccb00b50ef3dede7db3df3_image%20366.avif",
            "bgClass": "full-1",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/686fa0cb31912b109ce75f1a_Intangible-app-screenshot-final.avif",
            "logoContainerClass": "size_m",
            "imageClass": "image sie_big",
            "isSizeM": True
        },
        {
            "id": "superannotate",
            "name": "SuperAnnotate",
            "tagline": "Data OS for foundational AI models",
            "url": "https://www.superannotate.com/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/66ab8a0c5c3ade1f7d8b23ae_superanotate.svg",
            "bgClass": "full-5",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/66accbb2d0906511d8e76cc4_Frame%203.avif",
            "logoContainerClass": "size_m",
            "imageClass": "image",
            "isSizeM": False
        },
        {
            "id": "matchday",
            "name": "Matchday",
            "tagline": "The game for football's 5B fans",
            "url": "https://matchday.com/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/634a44acc8b9e2704379bf7e_matchday.png",
            "bgClass": "full",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/63728c8acbbfde0711aa05e6_Matchday-2.avif",
            "logoContainerClass": "size_m",
            "imageClass": "image",
            "isSizeM": False
        },
        {
            "id": "ac-momento",
            "name": "AC Momento",
            "tagline": "Football's Auction House",
            "url": "http://acmomento.com/",
            "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/633c20a94752ef155914a0e5_momento.svg",
            "bgClass": "full-3",
            "bgImageUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/686fa431086b1bfa34d0cdd3_momento.avif",
            "logoContainerClass": "size_m",
            "imageClass": "image momento",
            "isSizeM": False
        }
    ],
    "footer": {
        "logoUrl": "https://cdn.prod.website-files.com/633c180b60b06867471a6354/6346a74e759e2a8a337b0dd5_Playtime.svg",
        "email": "hello@playtime.vc",
        "socials": {
            "twitter": "https://twitter.com/playtime",
            "instagram": "https://www.instagram.com/playtime",
            "linkedin": "https://www.linkedin.com/company/playtimevc/"
        }
    },
    "press": [
        {
            "id": "press-1",
            "title": "Messi, Inc.",
            "text": "Lionel Messi’s upcoming $200MM fund and incubation studio lays the groundwork for a modern approach to capitalizing on singular talent.",
            "url": "https://generalist.com/briefing/messi"
        },
        {
            "id": "press-2",
            "title": "Bloomberg",
            "text": "Lionel Messi Launches Investment Firm Targeting Sports and Tech",
            "url": "https://www.bloomberg.com/news/articles/2022-10-19/lionel-messi-launches-investment-firm-targeting-sports-and-tech"
        },
        {
            "id": "press-3",
            "title": "TechCrunch",
            "text": "Soccer Legend Lionel Messi Plans to Get into Tech Investing via a New Silicon Valley Holding Company",
            "url": "https://techcrunch.com/2022/10/19/soccer-legend-lionel-messi-plans-to-get-into-tech-investing-via-a-new-silicon-valley-holding-company/amp/"
        },
        {
            "id": "press-4",
            "title": "Fast Company",
            "text": "Lionel Messi’s tech investment firm Play Time is betting big on this mobile gaming startup",
            "url": "https://www.fastcompany.com/90861956/lionel-messi-invests-matchday-mobile-gaming-startup-soccer"
        }
    ],
    "inquiries": []
}

def load_data():
    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {DATA_FILE}: {e}")
        return DEFAULT_DATA

def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving {DATA_FILE}: {e}")
        return False

class PlaytimeRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def send_json(self, status_code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        self.wfile.flush()

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def parse_body_json(self):
        content_len = int(self.headers.get("Content-Length", 0))
        if content_len == 0:
            return {}
        raw = self.rfile.read(content_len)
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception as e:
            return None

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        if not path:
            path = "/"

        # REST API Routes
        if path == "/api/content":
            data = load_data()
            return self.send_json(200, {"success": True, "data": data})

        elif path == "/api/hero":
            data = load_data()
            return self.send_json(200, {"success": True, "hero": data.get("hero", {})})

        elif path == "/api/portfolio":
            data = load_data()
            return self.send_json(200, {"success": True, "portfolio": data.get("portfolio", [])})

        elif path.startswith("/api/portfolio/"):
            comp_id = path.replace("/api/portfolio/", "")
            data = load_data()
            found = next((item for item in data.get("portfolio", []) if item.get("id") == comp_id), None)
            if found:
                return self.send_json(200, {"success": True, "company": found})
            return self.send_json(404, {"success": False, "error": "Company not found"})

        elif path == "/api/press":
            data = load_data()
            return self.send_json(200, {"success": True, "press": data.get("press", [])})

        elif path == "/api/footer":
            data = load_data()
            return self.send_json(200, {"success": True, "footer": data.get("footer", {})})

        elif path == "/api/settings":
            data = load_data()
            return self.send_json(200, {"success": True, "meta": data.get("meta", {})})

        elif path == "/api/inquiries":
            data = load_data()
            return self.send_json(200, {"success": True, "inquiries": data.get("inquiries", [])})

        elif path == "/api/export":
            data = load_data()
            body = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Disposition", 'attachment; filename="playtime_backup.json"')
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        # Fallback to serving static files
        super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        payload = self.parse_body_json()

        if payload is None:
            return self.send_json(400, {"success": False, "error": "Invalid JSON body"})

        data = load_data()

        # Update full content
        if path == "/api/content":
            save_data(payload)
            return self.send_json(200, {"success": True, "message": "Content updated", "data": payload})

        # Add Portfolio Company
        elif path == "/api/portfolio":
            if not payload.get("name"):
                return self.send_json(400, {"success": False, "error": "Company name is required"})
            
            comp_id = payload.get("id")
            if not comp_id:
                comp_id = payload["name"].lower().replace(" ", "-") + "-" + str(int(os.urandom(2).hex(), 16))
                payload["id"] = comp_id

            if "portfolio" not in data:
                data["portfolio"] = []
            
            data["portfolio"].append(payload)
            save_data(data)
            return self.send_json(201, {"success": True, "message": "Company added", "company": payload})

        # Reorder Portfolio
        elif path == "/api/portfolio/reorder":
            order_ids = payload.get("order", [])
            if isinstance(order_ids, list):
                curr = {item["id"]: item for item in data.get("portfolio", [])}
                reordered = [curr[i] for i in order_ids if i in curr]
                # append any missing
                for k, v in curr.items():
                    if k not in order_ids:
                        reordered.append(v)
                data["portfolio"] = reordered
                save_data(data)
                return self.send_json(200, {"success": True, "portfolio": data["portfolio"]})
            return self.send_json(400, {"success": False, "error": "Invalid order array"})

        # Add Press Item
        elif path == "/api/press":
            if not payload.get("title"):
                return self.send_json(400, {"success": False, "error": "Press title required"})
            if not payload.get("id"):
                payload["id"] = "press-" + str(int(os.urandom(2).hex(), 16))
            if "press" not in data:
                data["press"] = []
            data["press"].append(payload)
            save_data(data)
            return self.send_json(201, {"success": True, "message": "Press added", "press": payload})

        # Inbound Pitch Submission
        elif path == "/api/inquiries":
            if not payload.get("email") or not payload.get("company"):
                return self.send_json(400, {"success": False, "error": "Company and Email are required"})
            if not payload.get("id"):
                payload["id"] = "inq-" + str(int(os.urandom(3).hex(), 16))
            if "inquiries" not in data:
                data["inquiries"] = []
            data["inquiries"].insert(0, payload)
            save_data(data)
            return self.send_json(201, {"success": True, "message": "Inquiry submitted", "inquiry": payload})

        # Reset to Play Time Defaults
        elif path == "/api/reset":
            save_data(DEFAULT_DATA)
            return self.send_json(200, {"success": True, "message": "Reset to 100% Play Time defaults", "data": DEFAULT_DATA})

        # Import JSON Data
        elif path == "/api/import":
            if isinstance(payload, dict) and "portfolio" in payload:
                save_data(payload)
                return self.send_json(200, {"success": True, "message": "Data imported successfully", "data": payload})
            return self.send_json(400, {"success": False, "error": "Invalid backup structure"})

        return self.send_json(404, {"success": False, "error": f"Endpoint {path} not found"})

    def do_PUT(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        payload = self.parse_body_json()

        if payload is None:
            return self.send_json(400, {"success": False, "error": "Invalid JSON body"})

        data = load_data()

        # Update Hero Section
        if path == "/api/hero":
            data["hero"] = payload
            save_data(data)
            return self.send_json(200, {"success": True, "hero": data["hero"]})

        # Update Footer Section
        elif path == "/api/footer":
            data["footer"] = payload
            save_data(data)
            return self.send_json(200, {"success": True, "footer": data["footer"]})

        # Update Meta / Settings
        elif path == "/api/settings":
            data["meta"] = payload
            save_data(data)
            return self.send_json(200, {"success": True, "meta": data["meta"]})

        # Update specific portfolio company
        elif path.startswith("/api/portfolio/"):
            comp_id = path.replace("/api/portfolio/", "")
            port = data.get("portfolio", [])
            for i, comp in enumerate(port):
                if comp.get("id") == comp_id:
                    port[i] = {**comp, **payload, "id": comp_id}
                    save_data(data)
                    return self.send_json(200, {"success": True, "company": port[i]})
            return self.send_json(404, {"success": False, "error": "Company not found"})

        # Update specific press item
        elif path.startswith("/api/press/"):
            press_id = path.replace("/api/press/", "")
            press = data.get("press", [])
            for i, pr in enumerate(press):
                if pr.get("id") == press_id:
                    press[i] = {**pr, **payload, "id": press_id}
                    save_data(data)
                    return self.send_json(200, {"success": True, "press": press[i]})
            return self.send_json(404, {"success": False, "error": "Press item not found"})

        # Update specific inquiry status
        elif path.startswith("/api/inquiries/"):
            inq_id = path.replace("/api/inquiries/", "")
            inqs = data.get("inquiries", [])
            for i, inq in enumerate(inqs):
                if inq.get("id") == inq_id:
                    inqs[i] = {**inq, **payload, "id": inq_id}
                    save_data(data)
                    return self.send_json(200, {"success": True, "inquiry": inqs[i]})
            return self.send_json(404, {"success": False, "error": "Inquiry not found"})

        return self.send_json(404, {"success": False, "error": f"Endpoint {path} not found"})

    def do_DELETE(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        data = load_data()

        # Delete portfolio company
        if path.startswith("/api/portfolio/"):
            comp_id = path.replace("/api/portfolio/", "")
            original_len = len(data.get("portfolio", []))
            data["portfolio"] = [c for c in data.get("portfolio", []) if c.get("id") != comp_id]
            if len(data["portfolio"]) < original_len:
                save_data(data)
                return self.send_json(200, {"success": True, "message": f"Company {comp_id} deleted"})
            return self.send_json(404, {"success": False, "error": "Company not found"})

        # Delete press item
        elif path.startswith("/api/press/"):
            press_id = path.replace("/api/press/", "")
            original_len = len(data.get("press", []))
            data["press"] = [p for p in data.get("press", []) if p.get("id") != press_id]
            if len(data["press"]) < original_len:
                save_data(data)
                return self.send_json(200, {"success": True, "message": f"Press {press_id} deleted"})
            return self.send_json(404, {"success": False, "error": "Press item not found"})

        # Delete inquiry
        elif path.startswith("/api/inquiries/"):
            inq_id = path.replace("/api/inquiries/", "")
            original_len = len(data.get("inquiries", []))
            data["inquiries"] = [inq for inq in data.get("inquiries", []) if inq.get("id") != inq_id]
            if len(data["inquiries"]) < original_len:
                save_data(data)
                return self.send_json(200, {"success": True, "message": f"Inquiry {inq_id} deleted"})
            return self.send_json(404, {"success": False, "error": "Inquiry not found"})

        return self.send_json(404, {"success": False, "error": f"Endpoint {path} not found"})

def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, PlaytimeRequestHandler)
    print(f"Play Time API Server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
