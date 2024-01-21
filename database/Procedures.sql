CREATE PROCEDURE menaceFromBlacklist
(
	menaceNickname VARCHAR(20),
	blacklistID INTEGER,
	description VARCHAR(100),
	currentTown VARCHAR(1)
) AS
$$
	INSERT INTO menace
	VALUES
	(
		DEFAULT,
		menaceNickname,
		description,
		'tiger',
		(
			SELECT auth_date
		 	FROM blacklist
			WHERE id = blacklistID
			LIMIT 1
		),
		(
			SELECT town.id
		 	FROM blacklist
		 	JOIN person ON
		 		blacklist.person_id = person.id
		 	JOIN town ON
		 		town.id = person.town_id
		 	WHERE blacklist.id = blacklistID
		 	LIMIT 1
		),
		currentTown,
		'alive',
		TRUE,
		blacklistID
	);
$$
LANGUAGE SQL;