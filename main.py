import mvg_api

def time_of_day(milliseconds):
    """Convert milliseconds to datetime object and format as HH:MM:SS."""
    return mvg_api._convert_time(milliseconds).strftime("%X")


def main():
    start = "de:09162:9" # Laim
    dest = "de:09178:2680" # Freising
    connections = mvg_api.get_route(start, dest)

    for connection in connections:
        departure = connection["departure"]
        arrival = connection["arrival"]
        print("{}min".format(
                round((arrival - departure) / 1000 / 60),
        ))

        for part in connection["connectionPartList"]:
            line = "{}+{} -> {}+{} ".format(
                time_of_day(part["departure"]),
                part.get("delay", 0),
                time_of_day(part["arrival"]),
                part.get("arrDelay", 0),
            )

            if part["connectionPartType"] == "FOOTWAY":
                line += "Footway"
            else:
                line += "[{}] {} {} ({})".format(
                    part["departurePlatform"],
                    part["product"],
                    part["label"],
                    part["destination"],
                )

            if part["cancelled"]:
                line = "CANCELLED! " + line

            if part["sev"]:
                line = "SEV!!! " + line

            print(line)

            for nt in part.get("notifications", []):
                if any(l["lineNumber"] == part["label"] for l in nt["lines"]):
                    print("  NOTE: " + nt["title"])

        print()


if __name__ == "__main__":
    main()
